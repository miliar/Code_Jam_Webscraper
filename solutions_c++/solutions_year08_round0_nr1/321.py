//Compile Command:
//        g++ A.cpp -o A
//Run Command:
//        ./A A-small.in A-small.out
//        ./A A-large.in A-large.out

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

//switch rule: least and latest

int min(int *p, int len)
{
  int i = 0;
  int val = p[0];
  int index = 0;
  while(i < len-1) {
    i++;
    if (val > p[i]){
      index = i;
      val = p[i];
    }
  }
  return index;
}

int max(int *p, int len)
{
  int i = 0;
  int val = p[0];
  int index = 0;
  while(i < len-1) {
    i++;
    if (val < p[i]){
      index = i;
      val = p[i];
    }
  }
  return index;
}

void creatIndex(string *pKey, string *pEng, int *pKeyIndex, int *pEngCount, int *pEngCountForMin, int *pEngCurrent, int **ppEng, int key, int eng)
{
  for (int i = 0; i < eng; i++) {
    pEngCount[i] = 0;
    pEngCurrent[i] = 0;
    pEngCountForMin[i] = 0;
  }

  for (int i = 0; i < key; i++) {
    for (int j = 0; j < eng; j++) {
      if (pKey[i] == pEng[j]) {
	pKeyIndex[i] = j;
	pEngCount[j]++;
	pEngCountForMin[j]++;
	break;
      }
    }
  }

  for (int i = 0; i < eng; i++) {
    switch (pEngCount[i]){
    case 0:
      break;
    case 1:
      ppEng[i] = new int;
      break;
    default:
      ppEng[i] = new int[pEngCount[i]];
      break;
    }
  }

  int *ppEngIndex = new int[eng];
  for (int i = 0; i < eng; i++) {
    ppEngIndex[i] = 0;
  }

  for (int i = 0; i < key; i++) {
    ppEng[pKeyIndex[i]][ppEngIndex[pKeyIndex[i]]++] = i;
  }
  delete[] ppEngIndex;

}

void print(int *pKeyIndex, int *pEngCount, int *pEngCountForMin, int *pEngCurrent, int **ppEng, int key, int eng)
{
  for(int i = 0; i< eng; i++){
    cout << "Count:" << pEngCount[i] << endl;
  }
  for(int i = 0; i< eng; i++){
    cout << "Min:" << pEngCountForMin[i] << endl;
  }
  for(int i = 0; i< eng; i++){
    cout << "Current:" << pEngCurrent[i] << endl;
  }
  for(int i = 0; i< eng; i++){
    for(int j =0; j< pEngCount[i]; j++) {
      cout <<ppEng[i][j] << " ";
    }
    cout << endl;
  }
}

int switchEng(int *pKeyIndex, int *pEngCount, int *pEngCountForMin, int *pEngCurrent, int **ppEng, int key, int eng)
{
  //print(pKeyIndex, pEngCount, pEngCountForMin, pEngCurrent,ppEng, key, eng);
  int minIndex = min(pEngCountForMin, eng);
  int tmpIndex;
  int latest;
  int tmp;
  if (pEngCountForMin[minIndex] == 0) {
    return -1;
  }
  int *pTmp = new int[eng];
  for (int i =0 ; i<eng; i++) {
    pTmp[i] = ppEng[i][pEngCurrent[i]];
  }
  int maxIndex = max(pTmp, eng);
  delete[] pTmp;

  tmpIndex = pEngCurrent[maxIndex];
  latest = ppEng[maxIndex][tmpIndex];
 
  for (int i = 0; i < eng; i++) {
    for (int j = pEngCurrent[i]; j < pEngCount[i]; j++){
      if (ppEng[i][j] < latest) {
	pEngCurrent[i]++;
      }
      else{
	break;
      }
    }
  }
  
  for (int j = pEngCurrent[maxIndex]+1; j < pEngCount[maxIndex]; j++){
    if (ppEng[maxIndex][j] == (latest+1)) {
      pEngCurrent[maxIndex]++;
      latest++;
    }
    else{
      break;
    }
  }

  for (int i = 0; i < eng; i++) {
    pEngCountForMin[i] = pEngCount[i] - pEngCurrent[i];
  }
  return latest;
}

int main(int argc, char ** argv)
{
  ifstream infile(argv[1]);
  ofstream outfile(argv[2], ios::app);

  string aline("");
  int num;
  if (getline(infile,aline)) {
    num = atoi(aline.c_str());
  }
  int eng; int key;
  string *pEng, *pKey;
  for (int i=0; i < num; i++) {
    int count = 0;
    getline(infile,aline);
    eng = atoi(aline.c_str());
    pEng = new string[eng];
    for (int j = 0; j < eng; j++) { 
      getline(infile,aline);
      pEng[j] = aline;
    }
    getline(infile,aline);
    key = atoi(aline.c_str());
    if (key == 0) { count = 0;}
    else{
      pKey = new string[key];
      for (int j = 0; j < key; j++) { 
	getline(infile,aline);
	pKey[j] = aline;
      }
      int *pKeyIndex = new int[key];
      int *pEngCount = new int[eng];
      int *pEngCountForMin = new int[eng];
      int *pEngCurrent = new int[eng];
      int **ppEng = new int*[eng];

      creatIndex(pKey, pEng, pKeyIndex, pEngCount, pEngCountForMin, pEngCurrent, ppEng, key, eng);
      while(switchEng(pKeyIndex, pEngCount, pEngCountForMin, pEngCurrent, ppEng, key, eng) != -1) {
	count++;
      }
      for (int i = 0; i < eng; i++) {
	switch (pEngCount[i]){
	case 0:
	  break;
	case 1:
	  delete ppEng[i];
	  break;
	default:
	  delete[] ppEng[i];
	  break;
	}
      }
      delete[] ppEng;
      delete[] pKey;
      delete[] pKeyIndex;
      delete[] pEngCount;
      delete[] pEngCountForMin;
      delete[] pEngCurrent;
    }
    delete[] pEng;
    outfile << "Case #" << i+1 << ": " << count << endl;
    cout << "Case #" << i+1 << ": " << count << endl;
  }
  outfile.close();
  infile.close();
  return 0;
}
