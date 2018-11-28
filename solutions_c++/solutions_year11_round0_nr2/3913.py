#include<iostream>
#include<vector>
#include<string>
#include<map>
#include<algorithm>
using namespace std;
main()
{
  map<char,int> A;
  map<string,char> C;
  vector<int> D(8,0);
  vector<int> P(8,0);
  A['Q']=0;
  A['W']=1;
  A['E']=2;
  A['R']=3;
  A['A']=4;
  A['S']=5;
  A['D']=6;
  A['F']=7;
  int t;
  string str;
  cin>>t;
  for(int x=0;x<t;x++)
  {
    int c,d,n;
    cin>>c;
    C.clear();
    for(int i=0;i<c;i++)
    {
	cin>>str;
       // C[1<<A[str[0]]+1<<A[str[1]]]=str[2];
        string sub=str.substr(0,2);
	C[sub]=str[2];
        reverse(sub.begin(),sub.end());
	C[sub]=str[2];
    }
    cin>>d;
    for(int i=0;i<8;i++)
	D[i]=0;
    for(int i=0;i<d;i++)
    {
	cin>>str;
        D[A[str[0]]]|=1<<A[str[1]];
	D[A[str[1]]]|=1<<A[str[0]];
    }
    cin>>n;
    cin>>str;
    int p=0;
    for(int i=0;i<8;i++)
	P[i]=0;
    string out;
    for(int i=0;i<n;i++)
    {
       out.push_back(str[i]);
       //P[A[str[i]]]++;
       //p|=1<<A[str[i]];
       if(out.size()>1 && C.count(out.substr(out.size()-2))>0)
       {
	 if(--P[A[out[out.size()-2]]]==0)
            p^=1<<A[out[out.size()-2]];
         char q=C[out.substr(out.size()-2)];
	 out.erase(out.end()-2,out.end());
 	 out.push_back(q);
       }
       else if(D[A[str[i]]] && (D[A[str[i]]]&p)==D[A[str[i]]])
       {
         out.clear();
	 for(int j=0;j<8;j++)
	     P[j]=0;
	 p=0;
       }
       else
       {
       P[A[str[i]]]++;
       p|=1<<A[str[i]];
       }
    }
    cout<<"Case #"<<x+1<<": [";
    for(int i=0;i<out.size();i++)
    {
	if(i!=0)cout<<", ";
	cout<<out[i];
    }
    cout<<"]"<<endl;
  }
}
