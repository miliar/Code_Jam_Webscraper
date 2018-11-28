# include <iostream>
# include <string>

using namespace std;

void addTime(int inpTime[], int t) {
  if(inpTime[1] + t < 60)
    inpTime[1] += t;
  else {
    inpTime[0] += 1;
    inpTime[1] = inpTime[1] + t -60;
  }
}

int compareTime(int a[2], int b[2]) {
  // returns 1 if a is smaller or equal to b, else returns 0.
  if(a[0]<b[0]) return 1;
  else if(a[0]>b[0]) return 0;
  else if(a[1]<=b[1]) return 1;
  else return 0;
}

int main() {
  
  int noofcases, t, na, nb ;
  
  cin >> noofcases;
  int k, noA, noB, ans[noofcases][2];
  for(k=0;k<noofcases;k++) {
    cin>>t>>na>>nb;
    int depA[na][2], arrA[nb][2], depB[nb][2], arrB[na][2];
    string input;
    int i,j;
    for(i=0;i<na;i++) {
      cin>>input;
      depA[i][0]=atoi((input.substr(0,2)).c_str());
      depA[i][1]=atoi((input.substr(3,2)).c_str());
      cin>>input;
      arrB[i][0]=atoi((input.substr(0,2)).c_str());
      arrB[i][1]=atoi((input.substr(3,2)).c_str());
      addTime(arrB[i],t);
    }
      
    for(i=0;i<nb;i++) {
      cin>>input;
      depB[i][0]=atoi((input.substr(0,2)).c_str());
      depB[i][1]=atoi((input.substr(3,2)).c_str());
      cin>>input;
      arrA[i][0]=atoi((input.substr(0,2)).c_str());
      arrA[i][1]=atoi((input.substr(3,2)).c_str());
      addTime(arrA[i],t);
    }
      
    // Algorithm begins - computation of noA and noB.

    noA = na;
    noB = nb;
    int key, flagA[na], flagB[nb];
    for(i=0;i<na;i++)
      flagA[i]=0;
    for(i=0;i<nb;i++)
      flagB[i]=0;
      
    for(i=0;i<nb;i++) {
      key = -1;
      for(j=0;j<na;j++) {
	if( (compareTime(arrA[i], depA[j])==1) && (flagA[j]!=1) ) {
	  if(key ==-1)
	    key = j;
	  else if(compareTime(depA[j], depA[key])==1) 
	    key = j;
	}
	else ;
      }
	
      if(key !=-1) {
	flagA[key] =1;
	noA -= 1;
      }
    }
    
    for(i=0;i<na;i++) {
      key = -1;
      for(j=0;j<nb;j++) {
	if( (compareTime(arrB[i], depB[j])==1) && (flagB[j]!=1) ) {
	  if(key ==-1)
	    key = j;
	  else if(compareTime(depB[j], depB[key])==1) 
	    key = j;
	}
	else ;
      }
      if(key !=-1) {
	flagB[key] =1;
	noB -= 1;
      }
    }
    ans[k][0] = noA;
    ans[k][1] = noB;
  }
  for(k=0;k<noofcases;k++)
    cout<<"Case #"<<k+1<<": "<<ans[k][0]<<" "<<ans[k][1]<<endl;
  
  return 0;
}
