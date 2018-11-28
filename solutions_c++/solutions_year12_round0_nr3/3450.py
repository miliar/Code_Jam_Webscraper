#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
#include <string>
using namespace std;


int main (){
	int i,j,t=0,T, A, B, res,  length, temp1;
	int test;
	char *temp;
	temp=(char*)malloc(sizeof(int));
	freopen("data.in","r",stdin);
	freopen("data.out","w",stdout);
	cin >> T;
	while (t<T){
		cin >> A;
		cin >> B;
		res=0;
		itoa(A,temp,10);
		length=strlen(temp);
		j=A;
		if (length==1|| A==B) goto exit;

		while (j >= A && j <= B){
			for (i=1;i<length;i++){
				itoa(j,temp,10);
				rotate(temp,temp+i,temp+length);
				temp1=atoi(temp);
				if (temp1>j && temp1 <=B) res++;
			}
			j++;
		}
	exit:
	cout << "Case #" << ++t << ": " << res << endl;
	}

	return 0;
}
