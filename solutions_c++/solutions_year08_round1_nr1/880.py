
#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int compareinc(const void* f,const void* s){
  int* x = (int*) f;
  int* y = (int*) s;
  return(*x<*y);
}

int comparedec(const void* f,const void* s){
  int* x = (int*) f;
  int* y = (int*) s;
  return(*x>*y);
}


class testcase{
private:
  int n;
  int* f;
  int* s;

public:
  testcase(){
    f = (int*) malloc(sizeof(int)*802);
    s = (int*) malloc(sizeof(int)*802);
  }
  void changesize(int size){
    n = size;
  }

  void read(){
    for(int i = 0; i<n;i++)
      cin>>f[i];
    for(int i = 0; i<n;i++)
      cin>>s[i];
  }

  void solve(int caseno){
    qsort(f,n,sizeof(int),compareinc);
    qsort(s,n,sizeof(int),comparedec);
    int ans=0;
    for(int i=0;i<n;i++)
      ans = ans + (f[i]*s[i]);
    cout<<"Case #"<<caseno<<":"<<" "<<ans<<endl;
	
  }

  void show(){
    for(int i=0;i<n;i++)
      cout<<f[i]<<" "<<s[i]<<endl;
  }
};


int main(){
  int nofcases;
  int len=0;
  cin>>nofcases;
  testcase obj;
  for(int i = 1;i<=nofcases;i++){
    cin>>len;
    obj.changesize(len);
    obj.read();
    obj.solve(i);
  }
    
  return(0);
}


/*
int main(){
  testcase ob;
  ob.changesize(3);
  ob.read();
  ob.solve(1);
  ob.show();

  return(0);
}
*/
