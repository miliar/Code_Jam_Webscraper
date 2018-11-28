#include<iostream>
#include<vector>
#include<algorithm>
#include<set>
#include<string>
using namespace std;

int xp[]={1,0,-1,0};
int yp[]={0,1,0,-1};

bool test(int x1,int y1,int x2,int y2,const vector< pair<int,int> >& ps){
	int left,right,top,down;
	left=right=top=down=0;

	for(int i=0;i<ps.size()-1;i++){
		pair<int,int> pre=ps[i];
		pair<int,int> post=ps[i+1];

		if(pre.first>post.first || pre.second>post.second)
			swap(pre,post);

		if(pre.first==post.first){//horizon
			if(pre.second<=y1 && post.second>=y2){
				if(pre.first<=x1)top++;
				if(pre.first>=x2)down++;
			}
		}
		else{//vertical
			if(pre.first<=x1 && post.first>=x2){
				if(pre.second<=y1)left++;
				if(pre.second>=y2)right++;
			}
		}
	}

	//if(left+right+top+down>0)cout<<"KK"<<left<<" "<<right<<" "<<top<<" "<<down<<" "<<x1<<" "<<x2<<" "<<y1<<" "<<y2<<endl;
	if((left%2)==0 && (right%2)==0 && left!=0 && right!=0)return 1;
	if((top%2)==0 && (down%2)==0 && top!=0 && down!=0) return 1;

	return 0;
}

int main(){
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);

	//freopen("sample.txt","r",stdin);


	int n;
	cin>>n;
	for(int ca=1;ca<=n;ca++){
		int l;
		cin>>l;
		string path;
		for(int i=0;i<l;i++){
			string s;
			int t;
			cin>>s>>t;
			for(int j=0;j<t;j++)
				path+=s;
		}

		//cout<<path<<endl;

		int d=0;
		vector<int> xs,ys;
		vector< pair<int,int> > ps;
		

		xs.push_back(0);
		ys.push_back(0);
		ps.push_back(make_pair(0,0));

		int nowx=0;
		int nowy=0;
		for(int i=0;i<path.length();i++){
			if(path[i]=='F')nowx+=xp[d],nowy+=yp[d];
			else{
				xs.push_back(nowx);
				ys.push_back(nowy);
				ps.push_back(make_pair(nowx,nowy));

				if(path[i]=='R')d+=1;
				if(path[i]=='L')d+=3;

				d%=4;
			}
		}
		xs.push_back(nowx);
		ys.push_back(nowy);
		if(nowx!=0 || nowy!=0)cout<<"fxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxckfxck";
		ps.push_back(make_pair(0,0));

		//for(int i=0;i<ps.size();i++)cout<<ps[i].first<<" "<<ps[i].second<<endl;

		sort(xs.begin(),xs.end());
		sort(ys.begin(),ys.end());

		xs.erase(unique(xs.begin(),xs.end()),xs.end());
		ys.erase(unique(ys.begin(),ys.end()),ys.end());
		//for(int i=0;i<xs.size();i++)cout<<"X"<<xs[i];
		//for(int i=0;i<ys.size();i++)cout<<"y"<<ys[i];
		//cout<<endl;

		int ans=0;
		for(int i=0;i<xs.size()-1;i++){
			for(int j=0;j<ys.size()-1;j++){
				//cout<<"SB"<<endl;
				if(test(xs[i],ys[j],xs[i+1],ys[j+1],ps)){
					ans+=(xs[i+1]-xs[i])*(ys[j+1]-ys[j]);
					//cout<<"ans"<<ans<<endl;
				}
			}
		}

		//for(int i=-300;i<=300;i++){
		//	for(int j=-300;j<=300;j++){
		//		if(test(i,j,i+1,j+1,ps)){
		//			ans++;
		//			//cout<<"ans"<<ans<<endl;
		//		}
		//	}
		//}

		cout<<"Case #"<<ca<<": "<<ans<<endl;
		

	}
}