/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Albert Bendicho 2011 <albert.codejam@mailinator.com>
 * 
 */

#include<fstream>
using namespace std;

int main()
{
	fstream fin ("C-large.in", fstream::in);
	fstream fout ("C-large.out", fstream::out);
	int t;
	
	fin>>t;
	for (int it=0; it<t ; it++) {
		int n;
		long total,minimum,xored;
		total=0;
		minimum=1000001;
		xored=0;
		fin>>n;
		for (int in=0; in<n; in++) {
			int i;
			fin>>i;
			total+=i;
			xored^=i;
			minimum=(minimum>i?i:minimum);
		}
		fout<<"Case #"<<it+1<<": ";
		if (xored==0) fout<<(total-minimum); else fout<<"NO";
		fout<<endl;
	}
	return 0;
}