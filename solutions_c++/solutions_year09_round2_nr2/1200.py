#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
	int i,j,k,L,m,l;
	int T,N;
	int a[22],b[22],list[22];
	char c[22],buf;
	int temp=0;

	scanf("%d", &T);
	scanf("%c", &buf);
	for(l=0;l<T;l++)
	{
		gets(c);
		for(i=0;c[i]!='\0';i++){
			a[i]=c[i]-'0';
			b[i]=a[i]*(-1);
		}
		k=i;

		sort(b,b+k);
		for(i=0;i<k;i++)
			b[i]*=(-1);

		for(i=0;i<k;i++){
			if(a[i]!=b[i])
				break;
		}
		// 0추가해야함
		if(i==k){
			sort(b,b+k);
			if(b[0]!=0){
				b[k++]=0;
				sort(b,b+k);
				b[0]=b[1];
				b[1]=0;
				
			}
			else {
			temp=0;
			list[temp++]=b[0];
			for(i=1;i<k;i++){
				if(b[i]!=list[temp-1]){
					list[temp++]=b[i];
				}
			}
			L=temp;

			b[k++]=0;
			sort(b,b+k);
			for(i=0;i<k;i++){
				if(b[i]==list[1])
					break;
			}
			b[0]=b[i];
			b[i]=0;
			}
			printf("Case #%d: ", l+1);
			for(i=0;i<k;i++)
			{
				printf("%d", b[i]);
			}
			printf("\n");
			goto loop;


		}


		for(i=k-1;i>0;i--){
			if(a[i-1]>=a[i]);
			else{
				int temp;
				for(j=k-1;j>=i;j--){
					if(a[j]>a[i-1])
						break;
				}
				
				temp=a[j];
				a[j]=a[i-1];
				a[i-1]=temp;
				sort(a+i,a+k);
				break;
			}
		}


/*
		sort(b,b+k);
		temp=0;
		list[temp++]=b[0];
		for(i=1;i<k;i++){
			if(b[i]!=list[temp-1]){
				list[temp++]=b[i];
			}
		}
		L=temp;

		m=0;
		while(1){
			temp=0;
			for(i=0;i<k;i++){
				if(list[m]==a[i]){
					temp=i;
				}
			}
			if(temp<=k-1 || a[temp]>a[temp+1])
				break;
			else {
				m++;
				if(m>=L) break;
			}
		}


		int C=a[temp];
		a[temp]=a[temp+1];
		a[temp+1]=C;
*/

		printf("Case #%d: ", l+1);
		for(i=0;i<k;i++)
		{
			printf("%d", a[i]);
		}
		printf("\n");
		loop:;
	}

	return 0;
}