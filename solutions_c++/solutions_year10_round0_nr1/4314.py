#include <iostream>
#include <fstream>
using namespace std;
const int size=11;
int snap[size];
//int snapow[size];
#define DISK
int main(){
	int i,j,k,n,i1,i2,i3,cs,sun;
	bool flag=false,light=false;
	#ifdef DISK
	ifstream fin("A-small-attempt3.in");
	ofstream fout("A-small-attempt0.out");
	if(!fin||!fout){
		cout<<"can not open the file"<<endl;
		system("pause");
		return 1;
	}
	//typedef fin File;
	#else
	//typedef cin File;
	#endif
	fin>>cs;
	for(i=0;i<cs;i++){
		light=false;
		fin>>n;
		fin>>k;
		for(i1=0;i1<n;i1++){
			snap[i1]=0;
		}
		sun=0;
		for(j=0;j<k;j++){
			i2=0;
			light=false;
			while(i2<=sun){
				if(snap[i2]==1){
					snap[i2]=0;
				}
				else{
					snap[i2]=1;
				}
				i2++;
			}
			sun=0;i2=0;
			while(snap[i2]==1){
				sun++;
				i2++;
			}
			if(sun>=n)light=true;
			/*for(i2=0;i2<n;i2++){
				cout<<snap[i2]<<" ";
			}
			cout<<endl;*/
		}
		if(light){
				fout<<"Case #"<<i+1<<": ON"<<endl;
		}
		else{
			fout<<"Case #"<<i+1<<": OFF"<<endl;
		}
	}
//#ifndef DISK
	//system("pause");
   fin.close();
   fout.close();
	return 0;
}
				
				
				
	
