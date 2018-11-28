#include <cstdio>
#include <cstring>
#include <iostream>
#include <sstream>
#include <algorithm>
using namespace std;

char buf[30];
char buf2[30];

void swap(int i, int j)
{
	char t = buf[i];
	buf[i] = buf[j];
	buf[j] = t;
}

int asdf(const void *a, const void *b)
{
	return (*(char*)b - *(char*)a);
}

void aa()
{
	int len = strlen(buf);
	for (int j=1; j<len; ++j) {
		for (int i=0; i<j; ++i) {
			if (buf[j] < buf[i]) {
				swap(i, j);
				qsort(buf, j, sizeof(char), asdf);
				return;
			}
		}
	}
	buf[len] = '0';
	buf[len+1] = '\0';
	char c;
	int pos = -1;
	for (int i=0; i<len; ++i) {
		if (buf[i] != '0') {
			if (pos == -1) {
				c = buf[i];
				pos = i;
			}
			if (c > buf[i]) {
				c = buf[i];
				pos = i;
			}
		}
	}
	swap(len, pos);
	qsort(buf, len, sizeof(char), asdf);
}

int main()
{
	int N_;
	scanf("%d\n", &N_);
	for (int n_=1; n_<=N_; ++n_) {
		scanf("%s", buf2);
		int len = strlen(buf2);
		buf[len] = '\0';
		for (int i=0; i<len; ++i) {
			buf[len-1-i] = buf2[i];
		}
		aa();
		len = strlen(buf);
		for (int i=0; i<len; ++i) {
			buf2[len-1-i] = buf[i];
		}
		buf2[len] = '\0';
		printf("Case #%d: ", n_);
		printf("%s\n", buf2);
	}
	return 0;
}

