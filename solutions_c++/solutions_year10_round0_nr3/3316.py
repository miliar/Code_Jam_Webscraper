#pragma once

#include <iostream>
#include <string.h>
#include <cmath>

using namespace System;
using namespace System::IO;
using namespace std;

__int64 totalearn;
__int64 casee;

void get(System::IO::StreamReader ^in,StreamWriter ^out) {
	__int64 rides,seats,groups;
	__int64 qi = 0; //index

	String ^str = in->ReadLine();
	array<String^,1> ^line = str->Split(32);
	
	String ^str2 = in->ReadLine();
	array<String^,1> ^line2 = str2->Split(32);

	rides = Convert::ToInt32(line[0]);
	seats = Convert::ToInt64(line[1]);
	groups = Convert::ToInt64(line[2]);

	array<__int64^,1> ^q = gcnew array<__int64^,1>(groups);

	for(__int64 i=0;i<groups;i++) {
		q[i] = (__int64^)Convert::ToInt64(line2[i]);
		//cout<<(System::String)Convert::ToString(q[i]);
		//Console::Write(q[i] + " ");
	}

	//ride(groups,rides,seats);
     
	totalearn = 0;
	__int64 totalgrp = 0,curq = 0;
	bool rep = 0;
	for(__int64 i=0;i<rides;i++) {
		while(totalgrp <= seats) {
			if(curq == qi && rep == 1) {
				rep = 0;
				goto lbl;
			}
			if(totalgrp + (__int64)q[qi] <= seats)
				totalgrp = totalgrp + (__int64)q[qi++];
			else
				goto lbl;

			if(qi == groups) {
				qi = 0;
				rep = 1;
			}
			
		}
lbl:
		rep = 0;
		curq = qi;
		totalearn += totalgrp;
		totalgrp = 0;
	}
	
		out->Write("Case #");
		out->Write(Convert::ToString(casee));
		out->Write(": ");
		out->Write(Convert::ToString(totalearn));
		out->WriteLine("");


	
}

void main() {
	__int64 cases = 0;
	FileStream ^in = gcnew FileStream("C-small-attempt0.in",FileMode::Open,FileAccess::Read);
	FileStream ^out = gcnew FileStream("A-tem.out",FileMode::Create,FileAccess::ReadWrite);
	StreamReader ^sr = gcnew StreamReader(in);
	StreamWriter ^sw = gcnew StreamWriter(out);
	cases = Convert::ToInt32(sr->ReadLine());
	for(int i=0;i<cases;i++) {
		casee = i + 1;
		get(sr,sw);
	}

	cout<<"Complete"<<endl;
	cin>>totalearn;
	sr->Close();
	sw->Close();
	in->Close();
	out->Close();
}