#include <cstdio>
#include <vector>
#define pb(x) push_back((x))

using namespace std;

int abs(int x){
	return (x < 0)?-x:x;
}

int max(int a,int b){
	return (a<b)?b:a;
}

int main(){
	int z;
	scanf("%d",&z);
	for(int h=1;h<=z;h++){
		int n;
		scanf("%d",&n);
		int timeA1 = 0;
		int	timeA2 = 0;
		int timeB1 = 0;
		int timeB2 = 0;
		int posB;
		int posA = posB = 1;
		int timeMax = 0;
		int e;
		while(n--){
			char s[3];
			scanf("%s",s);
			int d;
			scanf("%d", &d);
			e = d;
			if(s[0] == 'O'){
				d = abs(d - posA);
				timeA1 = timeA2;
				timeA2 += d;
				posA = e;
				if(timeA2 < timeB2){
					timeA2 = timeB2 + 1;	
				} else {
					timeA2 += 1;
					timeMax = timeA2;
				}				
			} else {
				d = abs(d - posB);
				posB = e;
				timeB1 = timeB2;
				timeB2 += d;
				if(timeB2 < timeA2){
					timeB2 = timeA2 + 1;	
				} else {
					timeB2 += 1;
					timeMax = timeB2;
				}
			}
		}
		
		printf("Case #%d: %d\n",h,max(timeB2,timeA2));
		
	}
	return 0;
}
