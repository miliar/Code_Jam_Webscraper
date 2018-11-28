/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * main.cc
 * Copyright (C) Albert Bendicho 2011 <albert.codejam@mailinator.com>
 * 
 */

#include<fstream>
#include<stdlib.h>

using namespace std;

int main()
{
	fstream fin ("A-large.in", fstream::in);
	fstream fout ("A-large.out", fstream::out);
	int t,n,p;
	char r;
	int pos[2];
	int time[2];
	fin>>t;
	for (int it=0; it<t ; it++) {
		fin>>n;
		pos[0]=pos[1]=1;
		time[0]=time[1]=0;
		for (int in=0; in<n; in++) {
			fin>>r;
			fin>>p;
			int robot=(r=='O')?0:1;
			int timeinc=abs(pos[robot]-p)+1;
			if (time[robot^1]>=time[robot]+timeinc) {
				time[robot]=time[robot^1]+1;
			} else {
				time[robot]+=timeinc;
			};
			pos[robot]=p;
		}
		fout<<"Case #"<<it+1<<": "<<((time[0]>time[1])?time[0]:time[1])<<endl;
	}
	return 0;
}