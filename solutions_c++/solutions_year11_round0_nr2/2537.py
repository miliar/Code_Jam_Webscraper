#include <vector>
#include <iostream>

using namespace std;

void zeros(unsigned char a[256][256]){
	for (int x=0;x<256;x++)
		for (int y=0;y<256;y++)
			a[x][y]=0;
}

int main(){
	int T;
	cin>>T;
	for (int t=0;t<T;t++){
		int C=0, D=0, N=0;
		unsigned char opposed[256][256];
		unsigned char combines[256][256];
		vector <unsigned char> list;
		zeros(opposed);
		zeros(combines);
		
		cin>>C;
		for (int c=0;c<C;c++){
			unsigned char b1, b2, result;
			cin>>b1>>b2>>result;
			combines[b1][b2]=result;
			combines[b2][b1]=result;
		}

		cin>>D;
		for (int d=0;d<D;d++){
			unsigned char b1, b2;
			cin>>b1>>b2;
			opposed[b1][b2]=true;
			opposed[b2][b1]=true;
		}

		cin>>N;
		for (int n=0;n<N;n++){
			unsigned char b;
			cin>>b;
			list.push_back(b);

			//combinations/oppositions
			if (list.size()>=2){
				//combinations
				unsigned char toAdd = combines[list[list.size()-1]][list[list.size()-2]];
				if (toAdd!=0){
					list.pop_back();
					list.pop_back();
					list.push_back(toAdd);
				}
				
				//oppositions
				for (int i=0;i<list.size()-1;i++){
					if (opposed[list[i]][list[list.size()-1]]){
						list.clear();
						break;
					}
				}
			}
		}
		cout<<"Case #"<<(t+1)<<": [";
		for (int i=0;i<list.size();i++){
			cout<<list[i];
			if (i!=list.size()-1){
				cout<<", ";
			}
		}
		cout<<"]\n";
	}
}