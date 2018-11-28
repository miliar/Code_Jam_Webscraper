#include "stdafx.h"
#include <iostream>

using std::printf;
using std::scanf;
using System::Collections::Generic::List;
using System::Collections::Generic::Dictionary;

using namespace System;

FILE *stream;

int main(array<System::String ^> ^args)
{
	freopen_s(&stream, "D:\\Documents\\Misc\\CodeJam\\2011\\Data\\In\\B-large.in", "r", stdin);
	freopen_s(&stream, "D:\\Documents\\Misc\\CodeJam\\2011\\Data\\Out\\B-large.out", "w", stdout);
	int N = 0;
	scanf_s("%d", &N);
	for (int i = 1; i <= N; i++)
	{
		System::Text::StringBuilder^ answer = gcnew System::Text::StringBuilder("[");
		int C = 0;
		Dictionary<System::String^, System::String^> combinations = gcnew Dictionary<System::String^, System::String^>;
		scanf_s("%d ", &C);
		for (int j = 1; j <= C; j++)
		{
			System::Text::StringBuilder^ a = gcnew System::Text::StringBuilder;
			scanf("%s ", a);
			combinations.Add(a->ToString()->Substring(0, 2), a->ToString()->Substring(2, 1));
			if (a->ToString()->Substring(1, 1) != a->ToString()->Substring(0, 1))
				combinations.Add(a->ToString()->Substring(1, 1) + a->ToString()->Substring(0, 1), a->ToString()->Substring(2, 1));
		}
		int D = 0;
		List<System::String^>^ oppositions = gcnew List<System::String^>;
		scanf_s("%d ", &D);
		for (int j = 1; j <= D; j++)
		{
			System::Text::StringBuilder^ a = gcnew System::Text::StringBuilder;
			scanf("%s ", a);
			oppositions->Add(a->ToString()->Substring(0, 2));
		}				
		int n = 0;
		System::Char^ lastC = System::Convert::ToChar(" ");
		scanf_s("%d ", &n);
		for (int j = 1; j <= n; j++)
		{
			System::Text::StringBuilder^ c = gcnew System::Text::StringBuilder();
			System::Char^ thisC;
			scanf_s("%c", c);
			thisC = c[0];	
			if (combinations.ContainsKey(System::String::Concat(thisC, lastC)))
			{
				answer->Remove(answer->Length - 3, 3);
				answer->Append(combinations[System::String::Concat(thisC, lastC)][0]);
				lastC = combinations[System::String::Concat(thisC, lastC)][0];	
			}
			else
			{
				answer->Append(thisC);
				lastC = thisC;	
			}
			if (j < n)
				answer->Append(", ");
			for (int k = 0; k < oppositions->Count; k++)
				if (answer->ToString()->Contains(System::Convert::ToString(oppositions[k][0])) && answer->ToString()->Contains(System::Convert::ToString(oppositions[k][1])))
				{
					answer = gcnew System::Text::StringBuilder("[");
					lastC = System::Convert::ToChar(" ");
				}
		}	
		answer->Append("]");
		printf("Case #%d: %s\n", i, answer->ToString());
	}
    return 0;
}
