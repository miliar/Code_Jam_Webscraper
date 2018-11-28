// CodeJam2010.B.cpp : main project file.

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <memory>
#include <windows.h>
#include <vcclr.h>
//#include <ppl.h>
using namespace std;
//using namespace Concurrency;
using namespace System;
using namespace System::Numerics;
using namespace System::Threading::Tasks;
using namespace System::Runtime::InteropServices;
ifstream is("input.txt");
ofstream os("output.txt");

#include <functional> 

template<typename T> 
public ref class NativeFunctorWrapper { 
public: 
	NativeFunctorWrapper(T* p) : ptr_(p) {} 
	~NativeFunctorWrapper() { delete ptr_; } 
	void exec(int x) { 
		(*ptr_)(x); 
	} 
private: 
	T* ptr_; 
}; 

template <typename T> 
System::Action<T>^ make_action(std::function<void (T)> func) 
{ 
	typedef NativeFunctorWrapper<std::function<void (T)>> wrapper_t; 
	wrapper_t^ ptr = gcnew wrapper_t(new std::function<void (T)>(func)); 
	System::Action<T>^ f = gcnew System::Action<T>(ptr, &wrapper_t::exec); 
	return f; 
} 


void PrintAns(int i, const char* str) 
{
	os << "Case #" << i << ": " << str << endl;
}

int main(array<System::String ^> ^args)
{
	CRITICAL_SECTION sect;
//	is("input.txt");
//	os("output.txt");
	int T;
	is >> T;
	InitializeCriticalSection(&sect);
	for (int h=1; h<=T; ++h){
		int N, K;
		is >> N;
		array<BigInteger >^times = gcnew array<BigInteger >(1000);
		array<BigInteger >^ *times2 = &times;
		int times3 = (int) times2;
		BigInteger max=0;
		BigInteger x=0;
		BigInteger *x2=&x;
		int x3 = (int)x2;

		std::string s;
		for (int i=0; i<N;++i){
			is>>s;
			String^ S = gcnew String(s.c_str());;
			times[i]=BigInteger::Parse(S);
			if (max.CompareTo(times[i])<0)
				max=times[i];
		}
		auto f = [&](int i, int j){
			EnterCriticalSection(&sect);
			*(BigInteger *)x3 = BigInteger::GreatestCommonDivisor(*(BigInteger *)x3, (*(array<BigInteger >^ *)times3)[i]-(*(array<BigInteger >^ *)times3)[j]);
			LeaveCriticalSection(&sect);
		};

		Parallel::For(0, N, make_action<int>([&](Int32 i)->void{
			Parallel::For(i+1, N, make_action<int>([&](Int32 j)->void{
				f(i,j);
			}));
		}));
		BigInteger y = BigInteger::Remainder(BigInteger::Subtract(x,BigInteger::Remainder(max,x)),x);
		PrintAns(h, (char*)(void*)Marshal::StringToHGlobalAnsi(y.ToString()));
	}
	
//	parallel_for(0, T, [&](int i){
//	});
	return 0;
}

