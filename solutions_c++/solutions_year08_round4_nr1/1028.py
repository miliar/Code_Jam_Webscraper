#include<iostream>
#include<vector>

using namespace std;
// you can not type long long int
typedef long  lli;

lli eval(lli now,lli M,vector<lli>& vi){
	// AND
	if(now+1>(M-1)/2){
		return vi[now];
	}
	else if((now+1)*2+1>M){
		return eval((now+1)*2-1,M,vi);
	}
	else if(vi[now]==1){
		return (eval((now+1)*2-1,M,vi)&&eval((now+1)*2+1-1,M,vi));
	}
	else if(vi[now]==0){
		return (eval((now+1)*2-1,M,vi)||eval((now+1)*2+1-1,M,vi));
	}
}

void solve(lli num){
	lli i;
	lli M,V,tmp,bit;
	vector<lli> treeval;
	vector<lli> change;
	vector<lli> changeloc;
	cin >> M;
	cin >> V;
	bit=0;
	for(i=0;i<(M-1)/2;i++){
		cin >> tmp;
		treeval.push_back(tmp);
		cin >> tmp;
		change.push_back(tmp);
		if(tmp==1){
			bit++;
			changeloc.push_back(i);
		}
	}
	for(i=(M-1)/2;i<M;i++){
		cin >> tmp;
		treeval.push_back(tmp);
	}
	//
	lli limit=1;
	lli min=-1;
	lli j,needshift,changenum;
	for(i=0;i<bit;i++)limit*=2;
	for(i=0;i<limit;i++){
		needshift=i;
		changenum=0;
		for(j=0;j<bit;j++){
			if(needshift%2==1){
				treeval[changeloc[j]]=(treeval[changeloc[j]]+1)%2;
				changenum++;
			}
			needshift=needshift>>1;
		}
		
		if(min!=-1&&changenum>min){
		}
		else if(eval(0,M,treeval)==V){
			if(min==-1)min=changenum;
			else if(min>changenum)min=changenum;
		}
		
		needshift=i;
		changenum=0;
		for(j=0;j<bit;j++){
			if(needshift%2==1){
				treeval[changeloc[j]]=(treeval[changeloc[j]]+1)%2;
				changenum++;
			}
			needshift=needshift>>1;
		}
	}
	
	if(min==-1)cout << "Case #" << num << ": IMPOSSIBLE" << endl;
	else cout << "Case #" << num << ": " << min << endl;
}

int main(int argc,char** argv){
	int i;
	int cases;
	cin >> cases;
	for(i=0;i<cases;i++)solve(i+1);
	return 0;
}
