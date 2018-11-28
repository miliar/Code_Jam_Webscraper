// CTest.cpp : main project file.
#include "stdafx.h"

using namespace System;

ref struct stage {
	wchar_t Robot;
	int Button;
};

int next(System::Collections::Generic::List<stage^> ^st, int from, char R) {
	for (int i=from; i<st->Count; i++) {
		if (st[i]->Robot == R) return st[i]->Button;
	}
	return 0;
}

int solve(System::Collections::Generic::List<stage^> ^st) {
	int time = 0;
	int CB = 1, CO = 1, NB = 1, NO = 1;
	bool PB=false, PO=false;
	for (int i=0; i<st->Count; i++) {
		NB = next(st, i, 'B');
		NO = next(st, i, 'O');
		while(true) {
			//go to the next button, push
			if (NO && CO != NO) {
				CO>NO ? CO-- : CO++ ;
				//Console::WriteLine("O move in " + CO + " | " + NO);
			}else if (NO && st[i]->Robot=='O') {
				//push
				PO = true;
				//Console::WriteLine("O push " + CO);
			} else {
				//Console::WriteLine("O stay in " + CO);
			}

			if (NB && CB != NB) {
				CB>NB ? CB-- : CB++ ;
				//Console::WriteLine("B move in " + CB + " | " + NB);
			}else if (NB && st[i]->Robot=='B') {
				//push
				PB = true;
				//Console::WriteLine("B push " + CB);
			}else {
				//Console::WriteLine("B stay in " + CB);
			}

			time++;
			if (PO || PB) break;
		}
		PO = PB = false;
	}
	return time;
}

int main(array<System::String ^> ^args) {
    //load file
	System::IO::StreamReader^ file = gcnew System::IO::StreamReader("input.txt");
	int cases_count = Int32::Parse(file->ReadLine()), stages_count=0;
	System::String ^tmp = "";
	System::String ^res = "";
	for (int i=0; i<cases_count; i++) {
		tmp = file->ReadLine();
		tmp = tmp->Trim();
		array<String^> ^st;
		st = tmp->Split(' ');
		stages_count = Int32::Parse(st[0]);
		System::Collections::Generic::List<stage^> ^cases = gcnew System::Collections::Generic::List<stage^>();
		for (int j=1; j<st->Length; j+=2) {
			stage^ cur_stage = gcnew stage();
			cur_stage->Robot = st[j][0];
			cur_stage->Button = Int32::Parse(st[j+1]);
			cases->Add(cur_stage);
		}
		res += 	"Case #" + (i+1) + ": " + solve(cases) + "\r\n";
	}
	file->Close();
	System::IO::StreamWriter^ fileW = gcnew System::IO::StreamWriter("output.txt");
	fileW->Write(res);
	fileW->Close();
	Console::Write(res);
	Console::ReadKey();
    return 0;
}
