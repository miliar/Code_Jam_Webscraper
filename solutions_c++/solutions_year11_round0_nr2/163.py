#include<iostream>
#include<vector>
using namespace std;
string computeans(vector<string> sc,vector<string> so,string str) {
    int i,j,flag,k;
    string ans,newans;
    char tmp,tstri;
    for(i=0;i<str.size();i++) {
	tstri=str[i];
	if(ans.size()==0) {
	    ans=ans+str[i];
	    continue;
	}
	flag=1;
	tmp=ans[ans.size()-1];
	for(j=0;j<sc.size();j++) {
	    if(max(tmp,tstri)==max(sc[j][0],sc[j][1])&&min(tmp,tstri)==min(sc[j][0],sc[j][1])) {
		flag=0;
		ans[ans.size()-1]=sc[j][2];
		break;
	    }
	}
	if(flag==0) continue;
	flag=1;
	for(j=0;j<so.size();j++) {
	    for(k=0;k<ans.size();k++) {
		tmp=ans[k];
		if(max(tmp,tstri)==max(so[j][0],so[j][1])&&min(tmp,tstri)==min(so[j][0],so[j][1])) {
		    flag=0;
		    ans="";
		    break;
		}
	    }
	    if(flag==0) break;
	}
	if(flag==0) continue;
	ans=ans+str[i];
    }
    newans="[";
    for(i=0;i<ans.size();i++) {
	if(i==0) newans=newans+ans[i];
	else newans=newans+", "+ans[i];
    }
    newans=newans+"]";
    return newans;
}
void computeinstance(int thiscase) {
    int c,d,n,i;
    string scstr,sostr,strstr,ans,str;
    vector<string> sc,so;
    cin>>c;
    for(i=0;i<c;i++) {
	cin>>scstr;
	sc.push_back(scstr);
    }
    cin>>d;
    for(i=0;i<d;i++) {
	cin>>sostr;
	so.push_back(sostr);
    }
    cin>>n;
    cin>>str;
    ans=computeans(sc,so,str);
    cout<<"Case #"<<thiscase<<": "<<ans<<endl;
}
int main(void) {
    int t;
    cin>>t;
    for(int i=0;i<t;i++) {
	computeinstance(i+1);
    }
}
