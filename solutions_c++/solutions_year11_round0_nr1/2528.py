#include <fstream>

using namespace std;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t,it,n,i,cp1,cp2,tp1,tp2,free_t1,free_t2,p,time=0;
	char c;
	fin>>t;
	for(it=0;it<t;++it){
		cp1=1;
		cp2=1;
		free_t1=0;
		free_t2=0;
		time=0;

		fin>>n;
		for(i=0;i<n;++i){
			fin>>c>>p;
			switch(c){
				case 'O':
					tp1=p;
					if(free_t1<abs(tp1-cp1)){
						time+=(abs(tp1-cp1)-free_t1);
						free_t2+=(abs(tp1-cp1)-free_t1);
					}
					free_t1=0;
					time++;
					free_t2++;

					cp1=tp1;

					break;
				case 'B':
					tp2=p;
					if(free_t2<abs(tp2-cp2)){
						time+=(abs(tp2-cp2)-free_t2);
						free_t1+=(abs(tp2-cp2)-free_t2);
						free_t2=0;
					}
					free_t2=0;
					time++;
					free_t1++;

					cp2=tp2;

					break;
			}
		}
		fout<<"Case #"<<it+1<<": "<<time<<endl;
	}
	return 0;
}