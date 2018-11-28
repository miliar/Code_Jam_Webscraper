#include <cstdio>
#include <cstdlib>
#include <iostream>

#include <cstdio> 
#include <cstdlib> 
#include <iostream> 
#include <algorithm> 
#include <vector> 
#include <list> 
#include <map> 
#include <utility> 
#include <sstream> 
#include <string> 
#include <cstring> 
#include <cctype> 
#include <cmath> 
#include <queue> 
#include <stack> 
#include <set> 
 
using namespace std;


//int memo[1003][504];
//
//int TENGO;
//int n;
//int INF=(1<<30);
//int arr[1003];
//
//bool com(int a,int b){
//	return a>b;
//}
//
//int go(int pos,int tengo,int dejo){
//	
//	if(dejo > tengo)
//		return INF;
//	
//	if(pos>=n){
//		if(tengo==TENGO)
//			return 0;
//		return INF;
//	}
//	
//	if(tengo > TENGO)
//		return INF;
//
//	if(memo[pos][tengo]!=-1)
//		return memo[pos][tengo];
//	
//	int res=INF;
//	
//	res=min(res,arr[pos]+go(pos+1,tengo+1,dejo));
//	res=min(res,go(pos+1,tengo,dejo+1));
//
//	return memo[pos][tengo]=res;
//}
//int main(){
//
//	scanf("%d",&n);
//	
//	memset(memo,-1,sizeof memo);
//	
//	TENGO=n/2+n%2;
//
//	int val;
//	
//	for(int i=0;i<n;i++)
//		scanf("%d",&arr[i]);
//	sort(arr,arr+n,com);
//	int res=go(0,0,0);
//	cout<<res<<endl;
//	return 0;
//}

#define all(v) v.begin(),v.end()
//int n;
//long long arr[10003];
//int main(){
//	freopen ("C-large.txt","r",stdin);
//	freopen ("C2.out","w",stdout);
//	int cases;
//	cin>>cases;
//	//scanf("%d",&cases);
//	int t=1;
//	while(cases--){
//		cin>>n;
//		//scanf("%d",&n);
//		for(int i=0;i<n;i++)
//			cin>>arr[i];
//		bool pode=false;
//	
//		long long cade=0;
//		long long sum=0;
//		for(int i=0;i<n;i++){
//			cade^=arr[i];
//			sum+=arr[i];
//		}
//		
//		long long res=0,res1=0;
//		for(int i=0;i<n;i++){
//			res1=0;
//			for(int j=0;j<n;j++){
//				if(j==i)
//					continue;
//				res1^=arr[j];
//			}
//			if(res1==arr[i])
//				res=max(res,max(arr[i],sum-arr[i]));
//
//		}
//		cout<<"Case #"<<t++<<": "; 
//		if(cade)
//			cout<<"NO"<<endl;
//		else{
//			cout<<res<<endl;
//		}
//	}
//	return 0;
//}
//	
//int n;
//int	main(){
//	int cases;
		//freopen ("A-large.in","r",stdin);
		//freopen ("A2.out","w",stdout);
//	cin>>cases;
//	int t=1;
//	char c;
//	int bo;
//	while(cases--){
//		cin>>n;
//		vector <int> v1;
//		vector <char> v2;
//		for(int i=0;i<n;i++){
//			cin>>c>>bo;
//			v1.push_back(bo);
//			v2.push_back(c);
//		}
//		int res=0;
//		int fino=1;
//		int finb=1;
//		int tant=0;
//		char mov='X';
//		for(int i=0;i<v1.size();i++){
//			if(v2[i]=='O'){
//				if(v2[i]==mov){
//					res+=abs(v1[i]-fino)+1;
//					tant+=abs(v1[i]-fino)+1;
//					mov=v2[i];
//					fino=v1[i];
//					continue;
//					
//				}
//				int dis=abs(v1[i]-fino);
//				
//				if(dis-tant<=0)
//					dis=0;
//				else
//					dis-=tant;
//				res+=dis+1;
//				tant=dis+1;
//				fino=v1[i];
//				mov=v2[i];
//			}
//			else
//			{
//				if(v2[i]==mov){
//					res+=abs(v1[i]-finb)+1;
//					tant+=abs(v1[i]-finb)+1;
//					mov=v2[i];
//					finb=v1[i];
//					continue;
//					
//				}
//				int dis=abs(v1[i]-finb);
//				
//				if(dis-tant<=0)
//					dis=0;
//				else
//					dis-=tant;
//				res+=dis+1;
//				tant=dis+1;
//				finb=v1[i];
//				mov=v2[i];
//			}
//		}
//		cout<<"Case #"<<t++<<": ";
//		cout<<res<<endl;
//	}
//	return 0;
//}


using namespace std;

//int main()
//{
//  int cases;
//freopen ("B-large.in","r",stdin);
//freopen ("B2s.out","w",stdout);
//  cin>>cases;
//
//  int t=1;
//  map< pair<char,char>, char> pares;
//    set<pair<char,char> > todos;
//  while(cases--){
//
//    int m;
//    cin>>m;
//    pares.clear();
//    string cade;
//    for(int j=0; j<m;j++){
//		cin>>cade;
//		pares[make_pair(cade[0],cade[1])]=cade[2];
//		pares[make_pair(cade[1],cade[0])]=cade[2];
//    }
//    
//    int d;
//    cin>>d;
//    
//    todos.clear();
//    for(int j=0; j<d;j++){
//    cin>>cade;
//    todos.insert(make_pair(cade[0],cade[1]));
//    todos.insert(make_pair(cade[1],cade[0]));
//    }
//    
//    int n;
//    cin>>n;
//    string preg;
//    cin>>preg;
//    string ans="";
//    for(int j=0; j<n; j++)
//    {
//      if(ans.length()==0) 
//      ans+=preg[j];
//    else
//    {
//      if(pares.count(make_pair(ans[ans.length()-1],preg[j]))){
//          ans[ans.length()-1]=pares[make_pair(ans[ans.length()-1],preg[j])];
//          continue;
//      }
//      else if(pares.count(make_pair(preg[j],ans[ans.length()-1]))){
//		ans[ans.length()-1]=pares[make_pair(preg[j],ans[ans.length()-1])];
//          continue;
//      }
//      else 
//      {
//          int pos=-1;
//          for(int k=ans.length()-1; k>=0; k--)
//          {
//        if(todos.count(make_pair(ans[k],preg[j])) || todos.count(make_pair(preg[j],ans[k])))
//        {
//            pos=k;
//            break;
//        }
//          }
//          if(pos!=-1) 
//          {
//            ans="";
//            continue;
//          }
//       }
//       ans+=preg[j];
//    }
//    
//    }
//    
//    cout<<"Case #"<<t++<<": [";
//	if(ans.size())
//	cout<<ans[0];
//    for(int j=1; j<ans.length(); j++)
//      cout<<", "<<ans[j];
//    cout<<']'<<endl;
//  }
//  
//  return 0;
//}

int arr[1003];
int main(){

	int cases;
	freopen ("D-large.in","r",stdin);
	freopen ("D2.out","w",stdout);
	cin>>cases;
	int t=1;
	int n;

	while(cases--){
		cin>>n;
		int aux;
		int res=0;
		for(int i=1;i<=n;i++){
			cin>>aux;
			if(aux!=i)
				res++;
		}
		cout<<"Case #"<<t++<<": ";
		cout<<res<<endl;
	}
	return 0;
}