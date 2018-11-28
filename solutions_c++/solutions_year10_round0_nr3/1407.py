//Compiled in Dev-C++
#include<fstream>
#include<iostream>
using namespace std;

int main(char** argv, int argc){
    ifstream in("C-large.in");
    ofstream out("C-large.out");

	if(!in.good()||!out.good()){
		cout<<"AHHH!"<<endl;
		system("PAUSE");
	}

    int t;
    in>>t;
    for(int i=0;i<t;i++){  
            out<<"Case #"<<(i+1)<<": ";

            int r, n, k;
            in>>r;
            in>>k;
            in>>n;
            int* g = new int[n];
            unsigned long long * cost = new unsigned long long[n];
            int * next = new int[n];
            
            //initialize arrays
            for(int j=0; j<n; j++){
				in>>g[j];
				cost[j]=0;
				next[j]=0;
			}


			//start cycle
			for(int j=0;j<n;j++){
				if(cost[j]==0&&next[j]==j){
					cost[j]=g[j];
					next[j]=(next[j]+1)%n;
				}
				while(next[j]!=j &&cost[j]+g[next[j]] <= k){
					cost[j]+=g[next[j]];
					next[j] = (next[j]+1)%n;
				}


				if(j+1<n){
					cost[j+1] = cost[j] - g[j];
					next[j+1] = next[j];
				}
				
			}

			unsigned long long ans=0;
			int pt = 0;
			for(int j=0;j<r;j++){
				ans += cost[pt];
				pt = next[pt];
			}

            delete []g;
            delete[]cost;
            delete[]next;
            out<<ans<<endl;
   }
   in.close();
   out.close();
}
