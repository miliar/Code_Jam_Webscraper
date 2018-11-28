#include<iostream>
#include<vector>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int l,d,n;
    vector<string> dic,in;
    dic.resize(5001);
    in.resize(501);
    int i,j,k,ii,kk;
    int count;

    cin>>l>>d>>n;
    getchar();
    for(i=0;i<d;++i)
    {
	getline(cin,dic[i]);
    }
    for(i=0;i<n;++i)
    {
	cin>>in[i];
	bool flg=true;
	count = 0;
	for(ii=0;ii<d;++ii)
	{
	    flg=true;
	    k=0;
	    for(kk=0;kk<l;++kk)
	    {
		if(in[i][k]=='(')
		{
		    j=in[i].find(")",k);
		    string temp=in[i].substr(k,j-k+1);
		    k=j+1;
		    if(temp.find(dic[ii][kk]) == string::npos)
		    {
			flg=false;
//			cout<<dic[ii]<<"  ()\n";
//			cout<<k<<endl;
			break;
		    }
		}
		else
		{
		    if(in[i][k++] != dic[ii][kk])
		    {
			flg=false;
//			cout<<dic[ii]<<"  k\n";
			break;
		    }
		}
	    }
	    if(flg)
		count++;
	}
	cout<<"Case #"<<i+1<<": "<<count<<endl;
    }

}
