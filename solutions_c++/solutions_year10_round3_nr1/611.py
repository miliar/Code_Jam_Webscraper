// a.cpp: определяет точку входа для консольного приложения.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{
	FILE* F, *o;
	F = fopen("A-large.in", "r+");
	if(F==NULL)  return 1;
	o = fopen("A-large.out", "w+");
	int T;
	fscanf(F, "%d", &T);
	for(int t=0; t<T; t++){
		int n;
		fscanf(F, "%d", &n);
		int *f, *s;
		f = new int[n];
		s = new int[n];
		for(int i=0; i<n; i++)
			fscanf(F, "%d %d", &f[i], &s[i]);

		long per = 0;
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++){
				if(i==j) continue;
				if(f[i]>f[j] && s[j]>s[i]){
					per++;
					continue;
				}
				if(f[i]<f[j] && s[i]>s[j]){
					per++;
					continue;
				}
			};

		fprintf(o, "Case #%d: %d\n", t+1, per/2);

		delete f;
		delete s;
	}
	fclose(o);
	fclose(F);
	return 0;
}

