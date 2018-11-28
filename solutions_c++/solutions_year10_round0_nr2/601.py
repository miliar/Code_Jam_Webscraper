/*********************************************************************
  Author	  : AEQ
  Name		  : CStrInt
  Description : ���ڿ��� �� ������ ���/����/�� ���� ����
*********************************************************************/

#ifndef STRINT_OF_AEQ
#define STRINT_OF_AEQ

#pragma warning (disable:4996)		// C4996 : unsafe

#include <windows.h>				// MessageBox() - �����޽��� ���
#include <iostream>
#include <string>

#if 0					// "AEQ.h" ���� ������ 0���� ����
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
	CStrInt();								// �ʱ�ȭ ���� ���� �迭 �����
	CStrInt(const int nNum);				// ������ �����ʿ� int���� �� ��� �ڵ� ����ȯ ��
	CStrInt(const char *szN);				// ������ �����ʿ� ���ڿ��� �� ��� �ڵ� ����ȯ ��
	explicit CStrInt(const string &strN);	// explicit�� �����Ͽ� �ڵ� ����ȯ ����
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
	char m_chSign;				// ��ȣ
	string m_strN;				// �������� ����
};

END_AEQ

#endif	// STRINT_OF_AEQ
