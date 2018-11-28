#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

ifstream fin("try2.in");
ofstream fout("try2.out");

int T, n;
int const dim = 1000;
int mas1[dim];
int mas2[dim];

int answers[15];


void init(){
	for (int i=0;i<dim;i++){
		mas1[i]=0;
		mas2[i]=0;
	}
}

int intra(int numb){
	int sum=0;
	for (int i=0;i<n;i++)
		if (mas1[numb]<mas1[i]&&mas2[numb]>mas2[i])
			sum++;
	return sum;
}

int main(){
fin>>T;
int res;

for (int count=0;count<T;count++){
   init();
   res=0;
   fin>>n;
   for (int i=0;i<n;i++)
	   fin>>mas1[i]>>mas2[i];
    
   for (int i=0;i<n;i++)
      res = res + intra(i);

   //answers[count] = res;
   fout<<"Case #"<<count+1<<": "<<res<<endl;
}

    return 0;
}