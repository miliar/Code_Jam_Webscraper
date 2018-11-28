#pragma once

#include <iostream>
#include <string.h>
#include <cmath>

using namespace System;
using namespace System::IO;
using namespace std;

bool check(__int64 snaps,int snprs) {
	__int64 t = (__int64)pow((double)2,snprs) - 1;
	
	
	if(t == snaps%(t+1))
		return 1;
	else
		return 0;

}

__int64 snaps;
int snappers;
int casee = 1;
void get(System::IO::StreamReader ^in,StreamWriter ^out) {
	
	String ^str = in->ReadLine();
	array<String^,1> ^line = str->Split(32);

	snappers = Convert::ToInt32(line[0]);
	snaps = Convert::ToInt64(line[1]);
	
	if(check(snaps,snappers)) {
		out->Write("Case #");
		out->Write(Convert::ToString(casee));
		out->WriteLine(": ON"); }
	else {
		out->Write("Case #");
		out->Write(Convert::ToString(casee));
		out->WriteLine(": OFF"); }
}

int s,ss;
void main() {
	int cases = 0;
	FileStream ^in = gcnew FileStream("a-large.in",FileMode::Open,FileAccess::Read);
	FileStream ^out = gcnew FileStream("A-large.out",FileMode::Create,FileAccess::ReadWrite);
	StreamReader ^sr = gcnew StreamReader(in);
	StreamWriter ^sw = gcnew StreamWriter(out);
	cases = Convert::ToInt32(sr->ReadLine());
	for(int i=0;i<cases;i++) {
		casee = i + 1;
		get(sr,sw);
	}

	sr->Close();
	sw->Close();
	in->Close();
	out->Close();
}