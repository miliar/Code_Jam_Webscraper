#include <cstdio>
#include <cstring>


int main(){
	freopen("input.txt","r",stdin);
	freopen("C:\\Users\\ziroy\\Desktop\\output.txt","w",stdout);
	int count;
	char str[100];
	int ans[100];
	int mat[150];
	scanf("%d",&count);
	for (int _case=1;_case<=count;_case++){
		memset(mat,-1,sizeof(mat));
		int now = 0;
		scanf("%s",str);
		int len = strlen(str);
		mat[str[0]] = 1;
		ans[0] = 1;
		for (int i=1;i<len;i++){
			if (mat[str[i]] == -1){
				mat[str[i]] = now;
				ans[i] = mat[str[i]];
				now++;
				if (now == 1)
					now++;
			}
			else{
				ans[i] = mat[str[i]];
			}
		}
		__int64 sum = 0,d = 1;
		if (now == 0)
			now = 2 ;
		for (int i=len-1;i>=0;i--){
			sum += ans[i] * d;
			d *= now;
		}
		printf("Case #%d: %I64d\n",_case,sum);
	}
			
			

	return 0;
}