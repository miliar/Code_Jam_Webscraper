
#include <cstdio>
#include <iostream>
#include <string>
#include <map>

using namespace std;

int main(){
	
	int t; scanf("%d", &t);
	char buf[10000];
	map<int, int> form, oppo;
	char fin[10000], ptr;

	for(int x=1; x<=t; ++x){

		form.clear();
		oppo.clear();

		int n; scanf("%d", &n);

		for(int i=0; i<n; ++i){
			scanf("%s", buf);
			for(int j=0; j<3; ++j){
				buf[j] -= 'A';
			}
			form[buf[0]*26+buf[1]] = buf[2];
			form[buf[1]*26+buf[0]] = buf[2];
		}

		scanf("%d", &n);

		for(int i=0; i<n; ++i){
			scanf("%s", buf);
			buf[0] -= 'A';
			buf[1] -= 'A';
			oppo[buf[0]*26+buf[1]] = 1;
			oppo[buf[1]*26+buf[0]] = 1;
		}

		scanf("%d %s", &n, buf);

		for(int i=0; i<n; ++i){
			buf[i] -= 'A';
		}

		ptr = 0;

		for(int i=0; i<n; ++i){
			if(ptr == 0){
				fin[ptr++] = buf[i];
			}else{
				if(form.find(buf[i]*26+fin[ptr-1]) == form.end()){
					fin[ptr++] = buf[i];
				}else{
					fin[ptr-1] = form[buf[i]*26+fin[ptr-1]];
				}
				for(int j=0; j<ptr-1; ++j){
					if(oppo.find(fin[j]*26+fin[ptr-1]) != oppo.end()){
						ptr = 0;
						break;
					}
				}
			}
		}
		
		printf("Case #%d: [", x);
		
		for(int i=0; i<ptr; ++i){
			if(i==0){
				printf("%c", fin[i]+'A');
			}else{
				printf(", %c", fin[i]+'A');
			}
		}
		printf("]\n");
	}
	return 0;
}
