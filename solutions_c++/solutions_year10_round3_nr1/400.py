#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<vector>


using namespace std;
int ar[1002][2];
int N,T,sum;
vector<int> intersect;

int comp(const void *pa,const void *pb){
	int *a =(int *)pa;
	int *b = (int *) pb;
	if(a[0]==b[0])
		return b[1]-a[1];
	return b[0]-a[0];
}

int main(){
	cin >> T;
	for(int t=1;t<=T;t++){
		cin >> N;
		sum=0;
		for(int i=0;i<N;i++)
			cin >> ar[i][0] >> ar[i][1];
		for(int i=0;i<N;i++){
			intersect.clear();
			int negsize = 0;
			for(int j=0;j<N;j++)
				if((ar[i][0]-ar[j][0])*(ar[i][1]-ar[j][1])<0){
					bool b=true;
					for(int a=0;b && a < intersect.size();a++){
						int k=intersect[a];
						if((ar[i][0]-ar[j][0])*(ar[i][1]-ar[k][1]) == 
							 (ar[i][1]-ar[j][1])*(ar[i][0]-ar[k][0]))
							b=false;
					}
					if(b){
						intersect.push_back(j);
						if(j<i) negsize++;
					}
				}
			sum+=intersect.size()-negsize;
		}
		cout << "Case #" << t << ": " << sum << endl;
	}
}
