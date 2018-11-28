
#include<iostream>
#include<string>
#include<math.h>

using namespace std;

int mod(int n,int a){
  return(n%a > 0 ? (n%a) : (n%a)+a);
}

void printgstring(int n){
  cout<<"Case #"<<n<<": ";
}

class Seq{
private:
  int size;
  int* arr;
  int* next;
  int* prev;
public:
  Seq(){
    
  }
  void create(int n){
    arr = (int*) malloc(sizeof(int)*(n+1));
    next = (int*) malloc(sizeof(int)*(n+1));
    prev = (int*) malloc(sizeof(int)*(n+1));
    size = n;
    next[0]=1;
    for(int i =1;i<=size;i++){
      next[i]= mod(i+1,size);
      prev[i] = mod(i-1,size);
    }
      
  }
  void arrange(){
    
    int total = 0;
    int nowat=0;
    int count=1;
    
    int pudhe=count;
    
    while(total<size){
      pudhe = count;
      while(pudhe>0){
	nowat = next[nowat];
	pudhe--;
      }
      
      arr[nowat] = count;
      count=count+1;
      next[prev[nowat]]=next[nowat];
      prev[next[nowat]]=prev[nowat];
      total++;
      
    }
    
  }
  
  void show(){
    for(int i=1;i<=size;i++)
    cout<<arr[i]<<" ";
    cout<<endl;
  }

  int giveans(int n){
    return(arr[n]);
  }

};


int main(){
  int nofcases;
  Seq obj;
  int size;
  int nofqueries;
  int q;
  cin>>nofcases;
  
  for(int i =1;i<=nofcases;i++){
    cin>>size;
    obj.create(size);
    obj.arrange();
    cin>>nofqueries;
    printgstring(i);
    for(int j =1;j<=nofqueries;j++){
      cin>>q;
      cout<<obj.giveans(q)<<" ";
    }
    cout<<endl;
  }
  
  return(0);
}




