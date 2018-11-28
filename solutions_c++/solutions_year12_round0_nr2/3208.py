#include<iostream>
#include<vector>
using namespace std;
class Triplet{
	public:
		int low,mid,high;
		int tot;
		void print(){
			cout<<"("<<low<<","<<mid<<","<<high<<") ";
		}
		bool surprise(){
			if(high - low == 2) return true;
			else return false;
		}
};
bool cmp(Triplet a,Triplet b){
	int gapa = a.high - a.low;
	int gapb = b.high - b.low;
	if(gapa < gapb) return true;
	else return false;
}
int main(){
	Triplet t;
	vector< vector<Triplet> > v(31,vector<Triplet>());
	for(int i=0;i<11;i++)
		for(int j=i;j<(i+3<11?i+3:11);j++)
			for(int k=i;k<(i+3<11?i+3:11);k++){
				t.low = i;
				t.mid = j;
				t.high = k;
				t.tot = i+j+k;
				if(i<=j && j<=k)
					v[t.tot].push_back(t);
			}
	for(int i=0;i<31;i++){
		sort(v[i].begin(),v[i].end(),cmp);
	}
		
	int T;
	int N,S,p;
	cin>>T;
	int caseNum = 1;
	while(T--){
		cin>>N>>S>>p;
		vector<int> scores(N);
		for(int i=0;i<N;i++)
			cin>>scores[i];
		sort(scores.rbegin(),scores.rend());
		int ans = 0;
		for(int i=0;i<N;i++){
			int curr = scores[i];
//			cout<<"Checking score "<<curr<<endl;
			for(int i=0;i<v[curr].size();i++){
				if(v[curr][i].high >= p){
					if(v[curr][i].surprise() && (S > 0)){
						S--;
						ans++;
	//					cout<<"Picked "; v[curr][i].print();
						break;
					}
					else if(!v[curr][i].surprise()){
						ans++;
		//				cout<<"Picked "; v[curr][i].print();
						break;
					}
					else
						continue;
				}
			}
		}
		cout<<"Case #"<<caseNum++<<": "<<ans<<endl;				
	}
}

