/************************************************************************/
/* �ļ����ƣ�bigint.h
/* �ļ�������������ͷ�ļ�
/* �����ߣ��
/* ��ϵ��ʽ��yang_an19861217@126.com
/* ���˿ռ䣺hi.baidu.com/���̫��
/* ����ʱ�䣺 2009-10-05
/* �汾�ţ�1.0
/* �Ķ���¼��
/* ���뻷����vs 2005 + xp sp3
/************************************************************************/

#ifndef __bigint_H__
#define __bigint_H__

/************************************************************************/
/* ����ͷ�ļ����� */
#include <vector>
#include <iostream>
#include <string>

using namespace std;
/************************************************************************/

/************************************************************************/
/* ���������� */
class bigint
{
private:/*˽�б���*/
vector<int> cache_;/*��Ŵ���������*/
unsigned int len_;/*�����ĳ���*/

private:/*˽�к���*/
void delZeroFront_();/*ȥ�����������ǰ�������㣬���ȫΪ�㣬����һ����*/
void addZeroFront_(unsigned int len);/*����ǰ�油�㣬�������*/
void addZeroTail_(unsigned int len);/*�������油�㣬�൱�ڳ�10*/

public:/*���к���*/

/*���캯��*/
bigint();
bigint(string num);/*����Ϊstring*/
bigint(unsigned int len);/*��������Ϊlen��ֵΪȫ0*/

/*��������*/
~bigint();

/*���رȽ������*/
friend bool operator >(const bigint& lInt, const bigint& rInt);
friend bool operator >(const bigint& lInt, const string& str);
friend bool operator >(const string& str, const bigint& rInt);
friend bool operator <(const bigint& lInt, const bigint& rInt);
friend bool operator <(const bigint& lInt, const string& str);
friend bool operator <(const string& str, const bigint& rInt);
friend bool operator ==(const bigint& lInt, const bigint& rInt);
friend bool operator ==(const bigint& lInt, const string& str);
friend bool operator ==(const string& str, const bigint& rInt);

/*����������������*/
friend istream& operator >>(istream& in,bigint& bInt);
friend ostream& operator <<(ostream& out,const bigint& bInt);

/*���ؼӷ�*/
friend bigint operator +(const bigint& lInt, const bigint& rInt);
friend bigint operator +(const bigint& lInt, const string& str);
friend bigint operator +(const string& str, const bigint& rInt);

/*���ؼ���*/
friend bigint operator -(const bigint& lInt, const bigint& rInt);
friend bigint operator -(const bigint& lInt, const string& str);
friend bigint operator -(const string& str, const bigint& rInt);

/*���س˷�*/
friend bigint operator *(const bigint& lInt, const bigint& rInt);
friend bigint operator *(const bigint& lInt, const string& str);
friend bigint operator *(const string& str, const bigint& rInt);

/*���س���*/
friend bigint operator /(const bigint& lInt, const bigint& rInt);
friend bigint operator /(const bigint& lInt, const string& str);
friend bigint operator /(const string& str, const bigint& rInt);

/*�����෨*/
friend bigint operator %(const bigint& lInt, const bigint& rInt);
friend bigint operator %(const bigint& lInt, const string& str);
friend bigint operator %(const string& str, const bigint& rInt);

/*������*/
bigint poww(unsigned int n);
};
/************************************************************************/

#endif

bigint::bigint()
{
}

bigint::bigint(string num):
len_(0)
{
/*��ʼ��Ϊ��num��ʾ�Ĵ���*/
unsigned int len = num.length();
while (len)
{
   string strTmp = num.substr(len-1,1);
   const char* charTmp = strTmp.c_str();
   if (strcmp(charTmp,"0") < 0 || strcmp(charTmp,"9") > 0)
   {
    cout << "��ʼ��ʧ�ܣ�";
    exit(1);
   }
   cache_.push_back(atoi(charTmp));
   len--;
   len_++;
}
}

bigint::bigint(unsigned int len):
len_(len)
{
/*��ʼ��Ϊ����ΪlenȫΪ0�Ĵ���*/
while (len--)
{
   cache_.push_back(0);
}
}

bigint::~bigint()
{
/*��������*/
}

bool operator >(const bigint& lInt, const bigint& rInt)
{
/*����>�������1*/
bool flag = false;
if (lInt.len_ > rInt.len_)
{
   flag = true;
}
if (lInt.len_ == rInt.len_)
{
   unsigned int len = lInt.len_;
   while (len--)
   {
    if (lInt.cache_[len] > rInt.cache_[len])
    {
     flag = true;
     break;
    }
    if (lInt.cache_[len] < rInt.cache_[len])
    {
     break;
    }
   }
}
return flag;
}

bool operator >(const bigint& lInt, const string& str)
{
/*����>�������2*/
bigint tmp(str);
return (lInt > tmp);
}

bool operator >(const string& str, const bigint& rInt)
{
/*����>�������3*/
bigint tmp(str);
return (tmp > rInt);
}

bool operator <(const bigint& lInt, const bigint& rInt)
{
/*����<�������1*/
bool flag = false;
if (lInt.len_ < rInt.len_)
{
   flag = true;
}
if (lInt.len_ == rInt.len_)
{
   unsigned int len = lInt.len_;
   while (len--)
   {
    if (lInt.cache_[len] < rInt.cache_[len])
    {
     flag = true;
     break;
    }
    if (lInt.cache_[len] > rInt.cache_[len])
    {
     break;
    }
   }
}
return flag;
}

bool operator <(const bigint& lInt, const string& str)
{
/*����<�������2*/
bigint tmp(str);
return (lInt < tmp);
}

bool operator <(const string& str, const bigint& rInt)
{
/*����<�������3*/
bigint tmp(str);
return (tmp < rInt);
}

bool operator ==(const bigint& lInt, const bigint& rInt)
{
/*����==�������1*/
bool tmp = true;
if (lInt.len_ != rInt.len_)
{
   tmp = false;
}
else
{
   unsigned int len = lInt.len_;
   while (len--)
   {
    if (lInt.cache_[len] != rInt.cache_[len])
    {
     tmp = false;
     break;
    }
   }
}
return tmp;
}

bool operator ==(const bigint& lInt, const string& str)
{
/*����==�������2*/
bigint tmp(str);
return (lInt == tmp);
}

bool operator ==(const string& str, const bigint& rInt)
{
/*����==�������3*/
bigint tmp(str);
return (tmp == rInt);
}

istream& operator >>(istream& in,bigint& bInt)
{
/*�������������*/
string num;
//cout << "������һ��������";
in >> num;
bInt = num;
return in;
}

ostream& operator <<(ostream& out,const bigint& bInt)
{
/*������������*/
bigint tmp = bInt;
tmp.delZeroFront_();
unsigned int len = tmp.len_;
while (len--)
{
   out << tmp.cache_[len];
}
return out;
}

bigint operator +(const bigint& lInt, const bigint& rInt)
{
/*���ؼӷ���1*/
bigint lIntTmp = lInt;
bigint rIntTmp = rInt;
unsigned int lLen = lInt.len_;
unsigned int rLen = rInt.len_;
unsigned int count = 0;/*�������*/
int carry = 0;/*��λ����*/

if (lLen > rLen)
{
   bigint sumTmp(lLen);
   rIntTmp.addZeroFront_(lLen - rLen);
   while (count < lLen)
   {
    int carrySum = lIntTmp.cache_[count] + rIntTmp.cache_[count] + carry;
    sumTmp.cache_[count] = carrySum % 10;
    carry = carrySum / 10;
    count++;
   }
   if (carry > 0)
   {
    sumTmp.cache_.push_back(carry);
    sumTmp.len_++;
   }
   return sumTmp;
}
else
{
   bigint sumTmp(rLen);
   lIntTmp.addZeroFront_(rLen - lLen);
   while (count < rLen)
   {
    int carrySum = lIntTmp.cache_[count] + rIntTmp.cache_[count] + carry;
    sumTmp.cache_[count] = carrySum % 10;
    carry = carrySum / 10;
    count++;
   }
   if (carry > 0)
   {
    sumTmp.cache_.push_back(carry);
    sumTmp.len_++;
   }
   return sumTmp;
}
}

bigint operator +(const bigint& lInt, const string& str)
{
/*���ؼӷ���2*/
bigint tmp(str);
return (lInt + tmp);
}

bigint operator +(const string& str, const bigint& rInt)
{
/*���ؼӷ���3*/
bigint tmp(str);
return (tmp + rInt);
}

bigint operator -(const bigint& lInt, const bigint& rInt)
{
/*���ؼ�����1*/
if (lInt < rInt)
{
   cout << "��������";
   exit(1);
}
bigint subTmp(lInt.len_);
bigint lIntTmp = lInt;
bigint rIntTmp = rInt;
rIntTmp.addZeroFront_(lInt.len_-rInt.len_);
unsigned int count = 0;
while (count < lInt.len_)
{
   subTmp.cache_[count] = lIntTmp.cache_[count] - rIntTmp.cache_[count];
   if (subTmp.cache_[count] < 0)
   {
    subTmp.cache_[count] += 10;
    lIntTmp.cache_[count+1]--;
   }
   count++;
}
subTmp.delZeroFront_();
return subTmp;
}

bigint operator -(const bigint& lInt, const string& str)
{
/*���ؼ�����2*/
bigint tmp(str);
return (lInt - tmp);
}

bigint operator -(const string& str, const bigint& rInt)
{
/*���ؼ�����3*/
bigint tmp(str);
return (tmp - rInt);
}

bigint operator *(const bigint& lInt, const bigint& rInt)
{
/*���س˷���1*/
bigint lIntTmp = lInt,rIntTmp = rInt;
unsigned int len = lIntTmp.len_+rIntTmp.len_;
bigint ansTmp(len);

if (lInt.len_ < rInt.len_)
{
   lIntTmp = rInt;
   rIntTmp = lInt;
}
for (unsigned int count = 0; count < rIntTmp.len_; count++)
{
   bigint tmp(lIntTmp.len_+1);
   for (unsigned int i = 0; i < lIntTmp.len_; i++)
   {
    tmp.cache_[i] = lIntTmp.cache_[i] * rIntTmp.cache_[count];
   }
   tmp.addZeroTail_(count);
   ansTmp = ansTmp + tmp;
}
ansTmp.delZeroFront_();
return ansTmp;
}

bigint operator *(const bigint& lInt, const string& str)
{
/*���س˷���2*/
bigint tmp(str);
return (lInt * tmp);
}

bigint operator *(const string& str, const bigint& rInt)
{
/*���س˷���3*/
bigint tmp(str);
return (tmp * rInt);
}

bigint operator /(const bigint& lInt, const bigint& rInt)
{
/*���س�����1*/
bigint tmp("0");
if (lInt < rInt)
{
   tmp.cache_.push_back(0);
   tmp.len_ = 1;
}
else if (lInt == rInt)
{
   tmp = bigint("1");
}
else
{
   unsigned int len = lInt.len_ - rInt.len_ + 1;
   bigint lIntTmp = lInt,rIntTmp = rInt;
   bigint oTmp(len);
   while (len--)
   {
    while(rIntTmp * oTmp < lIntTmp)
    {
     oTmp.cache_[len]++;
    }
    if (oTmp.cache_[len] > 0)
    {
     oTmp.cache_[len]--;
    }
    tmp = tmp + oTmp;
    lIntTmp = lIntTmp - rIntTmp * oTmp;
    oTmp.cache_.erase(oTmp.cache_.end()-1);
    oTmp.len_--;
   }
}
return tmp;
}

bigint operator /(const bigint& lInt, const string& str)
{
/*���س�����2*/
bigint tmp(str);
return (lInt / tmp);
}

bigint operator /(const string& str, const bigint& rInt)
{
/*���س�����3*/
bigint tmp(str);
return (tmp / rInt);
}

bigint operator %(const bigint& lInt, const bigint& rInt)
{
/*�����෨��1*/
return (lInt - rInt * (lInt / rInt));
}

bigint operator %(const bigint& lInt, const string& str)
{
/*�����෨��2*/
bigint tmp(str);
return (lInt - tmp * (lInt / tmp));
}

bigint operator %(const string& str, const bigint& rInt)
{
/*�����෨��3*/
bigint tmp(str);
return (tmp - rInt * (tmp / rInt));
}

bigint bigint::poww(unsigned int n)
{
bigint oTmp(*this),tmp("1");
while (n--)
{
   tmp = tmp * oTmp;
}
return tmp;
}

void bigint::delZeroFront_()
{
/*ȥ�����������ǰ�������㣬���ȫΪ�㣬����һ����*/
if (len_ > 1)
{
   for (unsigned int len = len_; len > 1; len--)
   {
    if (cache_[len-1] == 0)
    {
     cache_.erase(cache_.end()-1);
     len_--;
    }
    else
    {
     break;
    }
   }
}
}

void bigint::addZeroFront_(unsigned int len)
{
/*����ǰ�油�㣬�������*/
while (len--)
{
   cache_.push_back(0);
   len_++;
}
}

void bigint::addZeroTail_(unsigned int len)
{
/*�������油�㣬�൱�ڳ�10*/
for (unsigned int i = 0; i < len; i++)
{
   cache_.push_back(0);
}
for (unsigned int i = len_+len-1; i > len - 1; i--)
{
   cache_[i] = cache_[i - len];
}
for (unsigned int i = 0; i < len; i++)
{
   cache_[i] = 0;
}
len_ += len;
}
