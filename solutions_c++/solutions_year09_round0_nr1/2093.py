// codejam1.cpp : main project file.
/* Program: Allien Language 
   Author: Victor H. Garcia
   For CodeJam 2009
*/
#include "stdafx.h"
#include <stdio.h>

using namespace System;
using namespace System::Text::RegularExpressions;

int main(array<System::String ^> ^args)
{
	System::IO::FileStream^ strm = gcnew System::IO::FileStream(args[0],System::IO::FileMode::Open);
	System::IO::StreamReader^ in = gcnew System::IO::StreamReader(strm);
	String^ line;
	array<String^>^  values;
	line = in->ReadLine();
	values = line->Split(L' ');
	int L = Convert::ToInt32(values[0]);
	int D = Convert::ToInt32(values[1]);
	int N = Convert::ToInt32(values[2]);
	int i;
	array<String^>^ words;
	array<String^>::Resize(words,D);
	for(i =0;i<D;i++){
		words[i] = in->ReadLine();
	}
	String ^tmp;
	int j, c;
	for(i = 1;i<=N;i++){
		tmp = in->ReadLine();
		tmp = tmp->Replace(L'(',L'[');
		tmp = tmp->Replace(L')',L']');
		c = 0;
		Regex^ r = gcnew Regex(tmp);
		for(j=0;j<D;j++){
			if(r->IsMatch(words[j])) c++;
		}
		Console::WriteLine("Case #" + i.ToString() + ": " + c.ToString());
	}
    return 0;
}
