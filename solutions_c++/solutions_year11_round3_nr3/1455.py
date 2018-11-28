#include "stdafx.h"
#include <stdio.h> 
#include <vector> 
#include <list>
#include <string>
#include <set>
#include <algorithm> 
#include <fstream> 
#include <iostream> 
#include <vcclr.h>
using namespace std;
using namespace System;
using namespace System::Numerics;
using namespace System::Threading::Tasks;
using namespace System::Runtime::InteropServices;


int main() 
{ 
	int T;
	cin >> T;
	array<BigInteger >^ nums = gcnew array<BigInteger >(10002);
	array<BigInteger >^ gcds = gcnew array<BigInteger >(10002);
	string s;
	for (int test = 1; test <= T; ++test)
	{
		int N;
		BigInteger L, H;
		string ls, hs;
		cin >> N >> ls >> hs;
		String^ S = gcnew String(ls.c_str());;
		L = BigInteger::Parse(S);
		S = gcnew String(hs.c_str());;
		H = BigInteger::Parse(S);
		
		for (int i = 1; i <= N; ++i)
		{
			cin >> s;
			S = gcnew String(s.c_str());;
			nums[i]=BigInteger::Parse(S);
		}
		Array::Sort(nums,1,N);

		S = nums[1].ToString();
		gcds[N] = nums[N];
		for (int i = N-1; i > 0; --i)
		{
			gcds[i] = BigInteger::GreatestCommonDivisor(nums[i], gcds[i+1]);
			S = gcds[i].ToString();
		}
		BigInteger lcm;
		lcm = 1;
		for (int i = 1; i <= N; ++i)
		{
			if (gcds[i] % lcm == BigInteger::Zero)
			{
				if (lcm > H || gcds[i] < L)
					goto sss;
				BigInteger a = lcm * (L/lcm);
				if (a<L) a+=lcm;
				//BigInteger s = BigInteger::Max(BigInteger::Min(gcds[i] / H, L), BigInteger::One);
				//BigInteger e = BigInteger::Max(gcds[i] / L, H);
				if (L*L <= gcds[i] )
				{
					BigInteger z;
					for (z = lcm * ((L-1)/lcm+1); z*z <= gcds[i] && z <= H; ++z)
					{
						if (gcds[i] % z == BigInteger::Zero && z % lcm == BigInteger::Zero)
						{
							lcm = z;
							goto ok;
						}
					}
					for (; gcds[i]/z <= H && gcds[i]/z >= L; --z)
						if (gcds[i] % (gcds[i]/z) == BigInteger::Zero && (gcds[i]/z) % lcm == BigInteger::Zero)
						{
							lcm = gcds[i]/z;
							goto ok;
						}
				}else
				{
					if (L*L > gcds[i] )
					{
						BigInteger z;
						for (z = gcds[i]/L; gcds[i]/z <= H && gcds[i]/z >= L; --z)
							if (gcds[i] % (gcds[i]/z) == BigInteger::Zero && (gcds[i]/z) % lcm == BigInteger::Zero)
							{
								lcm = gcds[i]/z;
								goto ok;
							}
					}
				}

				
// 				BigInteger z = gcds[i] / lcm;
// 				
// 				if (a*a < gcds[i])
// 				{
// 					while (a*a <= gcds[i] && a <= H)
// 					{
// 						if (gcds[i] % a == BigInteger::Zero)
// 						{
// 							lcm = a;
// 							goto ok;
// 						}
// 						a += lcm;
// 					}
// 				}
// 				else
// 				{
// 					while (a*a <= gcds[i] && a <= H)
// 					{
// 						if (gcds[i] % a == BigInteger::Zero)
// 						{
// 							lcm = a;
// 							goto ok;
// 						}
// 						a += lcm;
// 					}
// 				}
// 				BigInteger end = BigInteger::Min(H, gcds[i]);
				
			}
sss:
			lcm = lcm * nums[i] / BigInteger::GreatestCommonDivisor(lcm, nums[i]);
		}
		if (lcm >= L && lcm <= H)
			goto ok;
		BigInteger a = lcm * (L/lcm);
		if (a<L) a+=lcm;
		if (a<=H)
		{
			lcm = a;
			goto ok;
		}
no:
		cout << "Case #" << test << ": " << "NO" <<"\n";
		continue;

ok:
		cout << "Case #" << test << ": " << (char*)(void*)Marshal::StringToHGlobalAnsi(lcm.ToString()) <<"\n";
	}
#ifndef ONLINE_JUDGE
#ifndef FULLREDIRECT
	ifstream console("CONIN$");
	char fdasfadsfdasfdsa;
	console.getline(&fdasfadsfdasfdsa,1);
	console.close();
#endif
#endif
	return 0; 
}