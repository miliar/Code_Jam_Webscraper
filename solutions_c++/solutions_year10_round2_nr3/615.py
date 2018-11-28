#include <vector>
#include <iostream>

using namespace std;

inline bool check(char* ptr,int k) {

for(char* it=ptr;(*it)>0;it++) {
//if ((*it)>k) return false;
}

if ((*ptr)==0) return false;
if ((*ptr)==k) return true;

for(char* it=ptr;(*it)>0;it++) {
if ((*it)==k) {
    return check(ptr,(it-ptr)+1);
    }
}
return false;
}

int main() {

int N=25;
int count=1;
int CASE;
count=count<<(N-1);



vector<char> array;
array.resize((N-1)*count,0);

for(int i=0;i<count;i++) {
int k=0;
    for(int j=2;j<=N;j++) {
    if ((i>>(j-2))%2==1) {
       array[(N-1)*i+k]=j;
       k=k+1;
       }
    }
}


cin>>CASE;
for(int Case=1;Case<=CASE;Case++) {

int n;
cin>>n;

int maxI=1<<(n-1);
long result=0;
for(int i=0;i<maxI;i++) {
if (check( &(array[i*(N-1)]),n)) {result++;
				
//				for(int j=0;j<N-1;j++)
//			        cout<<array[i*(N-1)+j]<<" ";
//				cout<<endl;
				}
}

cout<<"Case #"<<Case<<": "<<(result%100003)<<endl;
}



}
