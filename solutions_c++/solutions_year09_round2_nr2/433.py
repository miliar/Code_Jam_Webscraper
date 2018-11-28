/**********************************************************************
Author: littlekid@whu
Created Time:  2009-9-13 0:10:02
File Name: 
Description: 
**********************************************************************/
#include <iostream>
#include <cstring>
using namespace std;

int main() 
{
	//freopen("F:\\ACM\\gcj2009\\R1B\\B.in", "r", stdin);
	freopen("F:\\ACM\\gcj2009\\R1B\\B.out", "w", stdout);
    int T;
	char num[24], ans[24];
	scanf("%d", &T);
	for (int ca = 1; ca <= T; ++ca) {
		scanf("%s", num);
		int len = strlen(num);
		bool flag = false;
		int pos;
		for (int ix = len-1; ix >= 0; --ix) {
			pos = ix;
			for (int jx = ix+1; jx < len; ++jx) {
				if (num[ix] < num[jx]) {
					if (!flag) {
						pos = jx;
					} else {
						if (num[pos] > num[jx]) {
							pos = jx;
						}
					}
					flag = true;
				}
			}
			if (flag) {
				swap(num[ix], num[pos]);
				sort(num+ix+1, num+len);
				break;
			}
		}
		if (!flag) {
			sort(num, num+len);
			for (int ix = len; ix > 0; --ix) {
				num[ix] = num[ix-1];
			}	
			num[1] = '0';
			num[len+1] = '\0';
			if (num[0] == '0') {
				for (int ix = 2; ix <= len; ++ix) {
					if (num[ix] != '0') {
						swap(num[0], num[ix]);
						break;	
					}
				}	
			}
		} 
		printf("Case #%d: %s\n", ca, num);
	}
    return 0;
}

