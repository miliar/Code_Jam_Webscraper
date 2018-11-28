#include<fstream>
#include<vector>
using namespace std;
ifstream fin("B-large.in");
ofstream fout("b.out");
int t,c,d,n,i,j,a1,a2,a3;
char c1,c2,c3;
int del[28][28],met[28][28],v[28];
vector<int> s;
int meta(){
	if(met[a1][s[s.size()-1]]!=0){
		v[s[s.size()-1]]--;
		v[met[a1][s[s.size()-1]]]++;
		s.push_back(met[a1][s[s.size()-1]]);
		s.erase(s.begin()+s.size()-2);
		return 1;
	}
	return 0;
}
int dlt(){
	for(int l=1;l<=26;l++)
		if(del[a1][l]==1&&v[l]!=0){
			s.clear();
			for(int l2=1;l2<=26;l2++)
				v[l2]=0;
			return 1;
		}
	return 0;
}
int main()
{
	fin>>t;
	for(j=1;j<=t;j++){
		for(int l=1;l<=26;l++)	for(int l2=1;l2<=26;l2++){del[l][l2]=met[l][l2]=0;}
		s.clear();
		for(int l=1;l<=26;l++)v[l]=0;
		fin>>c;
		for(i=1;i<=c;i++){
			fin>>c1>>c2>>c3;
			a1=(int)c1-'A'+1;
			a2=(int)c2-'A'+1;
			a3=(int)c3-'A'+1;
			met[a1][a2]=met[a2][a1]=a3;
		}
		fin>>d;
		for(i=1;i<=d;i++){
			fin>>c1>>c2;
			a1=(int)c1-'A'+1;
			a2=(int)c2-'A'+1;
			del[a1][a2]=del[a2][a1]=1;
		}
		fin>>n;
		fin>>c1;
		a1=(int)c1-'A'+1;
		s.push_back(a1);
		v[a1]++;
		for(i=2;i<=n;i++){
			fin>>c1;
			a1=(int)c1-'A'+1;
			if(s.size()>=1){
				if(meta()==0){
					if(dlt()==0){
						s.push_back(a1);
						v[a1]++;
					}
				}
			}
			else {
				s.push_back(a1);
				v[a1]++;
			}
		}
	fout<<"Case #"<<j<<": [";
	for(i=0;i<s.size();i++){fout<<char('A'+s[i]-1);
		if(i!=s.size()-1)fout<<", ";
	}
	fout<<']';
	fout<<'\n';
	}
	fin.close();
	fout.close();
	return 0;
}