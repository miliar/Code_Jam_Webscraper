#include<cstdio>
#include<vector>
#include<map>

using namespace std;

int main(){
  int T;
  scanf("%d\n",&T);
  for(int test=1;test<=T;test++){
    long long ans=0;
    int C,N,L;
    long long t;
    vector<int> a;
    vector<long long> b;
    map<int,int> num;
    long long l=0;
    scanf("%d%lld%d%d",&L,&t,&N,&C);
    b.push_back(0);
    for(int i=0;i<C;i++){
      int tmp;
      scanf("%d",&tmp);
      a.push_back(tmp);
      b.push_back(tmp+b[i]);
      l+=tmp;
    }

    if(t>=l*2*(N/C)){
       ans=l*2;
    }else{
      for(int i=0;i<C;i++){
	num[a[i]]+=(int)N/C-(int)t/(l*2);
	if(N%C>i)num[a[i]]++;
	if(b[i+1]*2<=t%(l*2)){
	  num[a[i]]--;
	}else{
	  if(b[i]*2<t%(l*2)){
	    num[a[i]]--;
	    num[a[i]-((t%(l*2)-b[i]*2)/2)]++;
	  }
	}
      }
      
      ans=t;
      map<int,int>::iterator itr=num.end();
      do{
	itr--;
	if(itr->second <= L){
	  L-=itr->second;
	  ans+=(itr->second) * (itr->first);
	}else{
	  ans+=L * (itr->first);
	  ans+=(itr->second - L) * (itr->first) *2;
	  L=0;
	}
      }while(itr!=num.begin());
    }
    printf("Case #%d: %lld\n",test,ans);
  }
  return 0;
}
