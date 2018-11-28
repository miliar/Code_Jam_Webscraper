/*********************************************************************
  Author	  : AEQ
  Name		  : CStrInt
  Description : 문자열로 된 정수의 산술/관계/논리 연산 지원
*********************************************************************/

#ifndef STRINT_OF_AEQ
#define STRINT_OF_AEQ

#pragma warning (disable:4996)		// C4996 : unsafe

#include <windows.h>				// MessageBox() - 에러메시지 출력
#include <iostream>
#include <string>

#if 0					// "AEQ.h" 파일 없으면 0으로 변경
	#include "AEQ.h"
#else
	#define BEGIN_AEQ
	#define END_AEQ
	#define USING_AEQ
#endif

using std::istream;
using std::ostream;
using std::string;

BEGIN_AEQ

//================================================================================
//                         class CStrInt
//================================================================================
class CStrInt {
public:
	/////////////////
	// constructor / destructor
	/////////////////
	CStrInt();								// 초기화 하지 않은 배열 선언용
	CStrInt(const int nNum);				// 연산자 오른쪽에 int형이 올 경우 자동 형변환 됨
	CStrInt(const char *szN);				// 연산자 오른쪽에 문자열이 올 경우 자동 형변환 됨
	explicit CStrInt(const string &strN);	// explicit로 선언하여 자동 형변환 방지
	CStrInt(const CStrInt &rBigN);
	virtual ~CStrInt();
	
	/////////////////
	// etc
	/////////////////
	size_t Size() const;
	CStrInt Abs() const;
	const string ToStr() const;

	/////////////////
	// unary operator overloading method
	/////////////////
	bool operator!() const;				// logical-negation
	CStrInt operator~() const;			// bitwise-negation (complement)
	CStrInt operator-() const;			// arithmetic-negation
	CStrInt &operator++();				// prefix incremental operator
	CStrInt operator++(int n);			// postfix incremental operator
	CStrInt &operator--();				// prefix decremental operator
	CStrInt operator--(int n);			// postfix decremental operator

	/////////////////
	// assignment operator overloading method
	/////////////////
	CStrInt &operator=(const CStrInt &rBigN);			// assignment
	CStrInt &operator+=(const CStrInt &rBigN);			// arithmetic
	CStrInt &operator-=(const CStrInt &rBigN);
	CStrInt &operator*=(const CStrInt &rBigN);
	CStrInt &operator/=(const CStrInt &rBigN);
	CStrInt &operator%=(const CStrInt &rBigN);

	/////////////////
	// binary operator overloading method
	/////////////////
	CStrInt operator+(const CStrInt &rBigN) const;		// arithmetic
	CStrInt operator-(const CStrInt &rBigN) const;
	CStrInt operator*(const CStrInt &rBigN) const;
	CStrInt operator/(const CStrInt &rBigN) const;
	CStrInt operator%(const CStrInt &rBigN) const;

	bool operator==(const CStrInt &rBigN) const;		// relational
	bool operator!=(const CStrInt &rBigN) const;
	bool operator<(const CStrInt &rBigN) const;
	bool operator>(const CStrInt &rBigN) const;
	bool operator<=(const CStrInt &rBigN) const;
	bool operator>=(const CStrInt &rBigN) const;

	bool operator&&(const CStrInt &rBigN) const;		// logical
	bool operator||(const CStrInt &rBigN) const;

	/////////////////
	// extractor / insertor
	/////////////////
	friend std::istream &operator>>(std::istream &_IN, CStrInt &rBigN);
	friend std::ostream &operator<<(std::ostream &_OUT, const CStrInt &rBigN);

private:
	enum EConstant {eBASE=10, eMAX_DIGIT=(sizeof(int)*3)};

	//////////////////////////////////////////////////////////////////////
	// four fundamental rules of arithmetics  of  unsigned number-string
	//////////////////////////////////////////////////////////////////////
	string _Add_Unsigned(const string &lhs, const string &rhs) const;
	string _Subtract_Unsigned(const string &lhs, const string &rhs) const;
	string _Multiply_Unsigned(const string &lhs, const string &rhs) const;
	string _Divide_Unsigned(const string &lhs, const string &rhs) const;
	string _Modulo_Unsigned(const string &lhs, const string &rhs) const;
	bool _Less_Unsigned(const string &lhs, const string &rhs) const;

	///////////////////////////
	// validity check
	///////////////////////////
	bool _IsValidChN(const char chN) const;
	void _VerifySzN(const char *szN) const;
	void _ShowErrorMsg(const char *szMsg) const;

private:
	char m_chSign;				// 부호
	string m_strN;				// 역순으로 저장
};

END_AEQ

#endif	// STRINT_OF_AEQ
