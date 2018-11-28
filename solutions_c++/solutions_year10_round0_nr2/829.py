#include <iostream>
#include <cstdio>

using namespace std;

long cgcd(long max, long min);
long absval(long val);

int main()
{
	int cases,c,n,i;
	long t[3],gcd,ans;
	FILE*fp;
	
	fp=fopen("googleOutput.txt","a");
	
	cin >> cases;
	for(c=1;c<=cases;c++){
		cin >> n;
		for(i=0;i<n;i++) cin >> t[i];
		
		switch( n ){
		
			case 2:
				gcd=(t[0]>t[1])?(t[0]-t[1]):(t[1]-t[0]);
				break;
			
			case 3:
				gcd=cgcd(absval(t[0]-t[1]),absval(t[1]-t[2]));
				break;
		}
		
		if((t[0]%gcd)==0) ans=0;
		else ans=gcd-t[0]%gcd;
		fprintf(fp,"Case #%d: %ld\n",c,ans);
	}
	fclose(fp);
	return 0;
		
}

long cgcd(long max, long min){

	long hold,m,n;
	m=max;
	n=min;
	max=(m>n)?m:n;
	min=(m<n)?m:n;
	
	while(min!=0){
		
		hold=min;
		min=max%min;
		max=hold;
		
	}
	
	return max;
	
}

long absval(long val)
{

	if(val>=0) return val;
	 
	 val*=-1;
	 return val;
	
}

