// CTest.cpp : main project file.
#include "stdafx.h"

using namespace System;

int sum(array<int> ^st, int count, int from, int to, bool xor) {
	int res=0;
	for (int i=from; i<to; i++)
		if (xor) res ^= st[i];
		else res += st[i];
	return res;
}

System::String^ solve(array<int> ^st, int count) {
	int sum_left, sum_right;
	for (int i=1; i<count; i++) {
		sum_left = sum(st, count, 0, i, true);
		sum_right = sum(st, count, i, count, true);
		if (sum_left == sum_right) return sum(st, count, i, count, false).ToString();
	}
	return "NO";
}

int main(array<System::String ^> ^args) {
    //load file
	System::IO::StreamReader^ file = gcnew System::IO::StreamReader("input.txt");
	int cases_count = Int32::Parse(file->ReadLine()), count=0;
	System::String ^tmp = "";
	System::String ^res = "";
	for (int i=0; i<cases_count; i++) {
		count = Int32::Parse(file->ReadLine());
		tmp = file->ReadLine();
		tmp = tmp->Trim();
		array<String^> ^st; array<int> ^candies = gcnew array<int>(count);
		st = tmp->Split(' ');
		for (int j=0; j<count; j++) candies[j] = Int32::Parse(st[j]);
		cli::array<int>::Sort(candies);
		res += 	"Case #" + (i+1) + ": " + solve(candies, count) + "\r\n";
	}
	file->Close();
	System::IO::StreamWriter^ fileW = gcnew System::IO::StreamWriter("output.txt");
	fileW->Write(res);
	fileW->Close();
	Console::Write(res);
	Console::ReadKey();
    return 0;
}
