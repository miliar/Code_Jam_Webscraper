//Compile Command:
//        g++ B.cpp -o B
//Run Command:
//        ./B B-small.in B-small.out
//        ./B B-large.in B-large.out

#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <cstdlib>

using namespace std;

class Train
{
public:
  int _on;
  int _dir;
  int _stime;
  int _etime;
  Train *_pnexttrain;
  Train(int dir, int stime, int etime)
  {
    _on = 0; // not available for scheduler
    _dir = dir;
    _stime = stime;
    _etime = etime;
    _pnexttrain = NULL;
  }
  void arrive()
  {
    _on = 1;
    _dir = 1-_dir;
  }

};

void sort(int *p1, int *p2, int *p3, int n)
{  
  int temp=0;  
  int i,j;  
  for(i=0;i<n-1;i++)   
    for(j=n-2;j>=i;j--)  
      if(p1[j]>p1[j+1])  
	{   
	  temp=p1[j];p1[j]=p1[j+1];p1[j+1]=temp;   
	  temp=p2[j];p2[j]=p2[j+1];p2[j+1]=temp;   
	  temp=p3[j];p3[j]=p3[j+1];p3[j+1]=temp;   
	}   
}

void clear(Train * pFirstTrain)
{
  Train *p1, *p2;
  p2 = pFirstTrain;
  p1 = p2->_pnexttrain;
  while(p1!=NULL){
    p2 = p1->_pnexttrain;
    delete p1;
    p1 = p2;
  }
  delete pFirstTrain;
}

void setTrains(Train * pFirstTrain, int start)
{
  Train *p;
  p = pFirstTrain;
  while(p!=NULL){
    if (p->_on == 0 && p->_etime <= start){
      p->arrive();
    }
    p = p->_pnexttrain;
  }
}

bool selTrain(Train * pFirstTrain, int dir, int start, int end)
{
  Train *p;
  p = pFirstTrain;
  bool flag = false;
  while(p!=NULL){
    if (p->_on == 1 && p->_dir == dir){
      flag = true;
      p->_on = 0;
      p->_stime = start;
      p->_etime = end;
      break;
    }
    else {
      p = p->_pnexttrain;
    }
  }
  return flag;
}

Train * addTrain(Train * pLastTrain, int dir, int start, int end)
{
  Train *p = new Train(dir,start,end);
  pLastTrain->_pnexttrain = p;
  return p;
}

void schedule(int *pa2b, int *pb2a, int a2b, int b2a, int counts[2])
{
  int *pstart = new int[a2b+b2a];
  int *pend = new int[a2b+b2a];
  int *pstartindex = new int[a2b+b2a];
  for(int i=0;i<a2b;i++){
    pstart[i]=pa2b[i*2];
    pend[i] = pa2b[i*2+1];
    pstartindex[i] = 0;
  }
  for(int i=0;i<b2a;i++){
    pstart[a2b+i]=pb2a[i*2];
    pend[a2b+i]=pb2a[i*2+1];
    pstartindex[a2b+i] = 1;
  }
  
  delete[] pa2b;
  delete[] pb2a;

  sort(pstart,pend,pstartindex,a2b+b2a);

  Train *pFirstTrain = new Train(pstartindex[0],pstart[0],pend[0]);
  Train *pLastTrain = pFirstTrain;
  counts[pstartindex[0]]++;
  Train *p;
  bool flag;

  for (int i = 1; i<a2b+b2a; i++){
    setTrains(pFirstTrain,pstart[i]);
    flag = selTrain(pFirstTrain,pstartindex[i],pstart[i],pend[i]);
    if (flag==false){
      pLastTrain = addTrain(pLastTrain,pstartindex[i],pstart[i],pend[i]);
      counts[pstartindex[i]]++;
    }
  }
  clear(pFirstTrain);
  delete[] pstart;
  delete[] pend;
  delete[] pstartindex;
}

int main(int argc, char ** argv)
{
  ifstream infile(argv[1]);
  ofstream outfile(argv[2], ios::app);

  string aline("");
  int num;
  int delay = 0;
  if (getline(infile,aline)) {
    num = atoi(aline.c_str());
  }
  for (int i=0; i < num; i++) {
    int counts[2]={0,0};
    if (getline(infile,aline)) {
      delay = atoi(aline.c_str());
    }
    int a2b, b2a;
    string stra2b,strb2a;
    string::size_type index;
    getline(infile,aline);
    index = aline.find(" ", 0);
    if (index != string::npos) {
      stra2b = aline.substr(0, index);
      strb2a = aline.substr(index+1, aline.length());
      a2b = atoi(stra2b.c_str());
      b2a = atoi(strb2a.c_str());
    }
    if (a2b==0 || b2a == 0){
      counts[0] = a2b; counts[1] = b2a;
      for (int j = 0; j<(a2b+b2a);j++){
	getline(infile,aline);
      }
    }
    else {
      string str1,str2;
      int *pa2b = new int[a2b*2];
      for(int j=0; j<a2b; j++){
	getline(infile,aline);
	index = aline.find(" ", 0);
	stra2b = aline.substr(0, index);
	strb2a = aline.substr(index+1, aline.length());

	index = stra2b.find(":", 0);
	str1 = stra2b.substr(0, index);
	str2 = stra2b.substr(index+1, stra2b.length());
	pa2b[j*2] = 60*atoi(str1.c_str())+atoi(str2.c_str());

	index = strb2a.find(":", 0);
	str1 = strb2a.substr(0, index);
	str2 = strb2a.substr(index+1, strb2a.length());
  	pa2b[j*2+1] = 60*atoi(str1.c_str())+atoi(str2.c_str())+delay;
      }
      int *pb2a = new int[b2a*2];
      for(int j=0; j<b2a; j++){
	getline(infile,aline);
	index = aline.find(" ", 0);
	stra2b = aline.substr(0, index);
	strb2a = aline.substr(index+1, aline.length());

	index = stra2b.find(":", 0);
	str1 = stra2b.substr(0, index);
	str2 = stra2b.substr(index+1, stra2b.length());
	pb2a[j*2] = 60*atoi(str1.c_str())+atoi(str2.c_str());

	index = strb2a.find(":", 0);
	str1 = strb2a.substr(0, index);
	str2 = strb2a.substr(index+1, strb2a.length());
  	pb2a[j*2+1] = 60*atoi(str1.c_str())+atoi(str2.c_str())+delay;
     }
      schedule(pa2b,pb2a,a2b,b2a,counts);
    }
    outfile << "Case #" << i+1 << ": " << counts[0] << " " << counts[1] << endl;
    cout << "Case #" << i+1 << ": " << counts[0] << " " << counts[1] << endl;
  }
  outfile.close();
  infile.close();
  return 0;
}
