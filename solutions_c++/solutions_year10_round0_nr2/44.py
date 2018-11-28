/************************************************************************/
/* 文件名称：bigint.h
/* 文件描述：大数类头文件
/* 创建者：杨安
/* 联系方式：yang_an19861217@126.com
/* 个人空间：hi.baidu.com/秀才太守
/* 创建时间： 2009-10-05
/* 版本号：1.0
/* 改动记录：
/* 编译环境：vs 2005 + xp sp3
/************************************************************************/

#ifndef __bigint_H__
#define __bigint_H__

/************************************************************************/
/* 常用头文件包含 */
#include <vector>
#include <iostream>
#include <string>

using namespace std;
/************************************************************************/

/************************************************************************/
/* 大数类声明 */
class bigint
{
private:/*私有变量*/
vector<int> cache_;/*存放大数的向量*/
unsigned int len_;/*大数的长度*/

private:/*私有函数*/
void delZeroFront_();/*去掉大数处理后前面多出的零，如果全为零，就留一个零*/
void addZeroFront_(unsigned int len);/*大数前面补零，方便计算*/
void addZeroTail_(unsigned int len);/*大数后面补零，相当于乘10*/

public:/*公有函数*/

/*构造函数*/
bigint();
bigint(string num);/*大数为string*/
bigint(unsigned int len);/*大数长度为len，值为全0*/

/*析构函数*/
~bigint();

/*重载比较运算符*/
friend bool operator >(const bigint& lInt, const bigint& rInt);
friend bool operator >(const bigint& lInt, const string& str);
friend bool operator >(const string& str, const bigint& rInt);
friend bool operator <(const bigint& lInt, const bigint& rInt);
friend bool operator <(const bigint& lInt, const string& str);
friend bool operator <(const string& str, const bigint& rInt);
friend bool operator ==(const bigint& lInt, const bigint& rInt);
friend bool operator ==(const bigint& lInt, const string& str);
friend bool operator ==(const string& str, const bigint& rInt);

/*重载输入输出运算符*/
friend istream& operator >>(istream& in,bigint& bInt);
friend ostream& operator <<(ostream& out,const bigint& bInt);

/*重载加法*/
friend bigint operator +(const bigint& lInt, const bigint& rInt);
friend bigint operator +(const bigint& lInt, const string& str);
friend bigint operator +(const string& str, const bigint& rInt);

/*重载减法*/
friend bigint operator -(const bigint& lInt, const bigint& rInt);
friend bigint operator -(const bigint& lInt, const string& str);
friend bigint operator -(const string& str, const bigint& rInt);

/*重载乘法*/
friend bigint operator *(const bigint& lInt, const bigint& rInt);
friend bigint operator *(const bigint& lInt, const string& str);
friend bigint operator *(const string& str, const bigint& rInt);

/*重载除法*/
friend bigint operator /(const bigint& lInt, const bigint& rInt);
friend bigint operator /(const bigint& lInt, const string& str);
friend bigint operator /(const string& str, const bigint& rInt);

/*重载余法*/
friend bigint operator %(const bigint& lInt, const bigint& rInt);
friend bigint operator %(const bigint& lInt, const string& str);
friend bigint operator %(const string& str, const bigint& rInt);

/*幂运算*/
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
/*初始化为用num表示的大数*/
unsigned int len = num.length();
while (len)
{
   string strTmp = num.substr(len-1,1);
   const char* charTmp = strTmp.c_str();
   if (strcmp(charTmp,"0") < 0 || strcmp(charTmp,"9") > 0)
   {
    cout << "初始化失败！";
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
/*初始化为长度为len全为0的大数*/
while (len--)
{
   cache_.push_back(0);
}
}

bigint::~bigint()
{
/*析构函数*/
}

bool operator >(const bigint& lInt, const bigint& rInt)
{
/*重载>运算符，1*/
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
/*重载>运算符，2*/
bigint tmp(str);
return (lInt > tmp);
}

bool operator >(const string& str, const bigint& rInt)
{
/*重载>运算符，3*/
bigint tmp(str);
return (tmp > rInt);
}

bool operator <(const bigint& lInt, const bigint& rInt)
{
/*重载<运算符，1*/
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
/*重载<运算符，2*/
bigint tmp(str);
return (lInt < tmp);
}

bool operator <(const string& str, const bigint& rInt)
{
/*重载<运算符，3*/
bigint tmp(str);
return (tmp < rInt);
}

bool operator ==(const bigint& lInt, const bigint& rInt)
{
/*重载==运算符，1*/
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
/*重载==运算符，2*/
bigint tmp(str);
return (lInt == tmp);
}

bool operator ==(const string& str, const bigint& rInt)
{
/*重载==运算符，3*/
bigint tmp(str);
return (tmp == rInt);
}

istream& operator >>(istream& in,bigint& bInt)
{
/*重载输入运算符*/
string num;
//cout << "请输入一个大数：";
in >> num;
bInt = num;
return in;
}

ostream& operator <<(ostream& out,const bigint& bInt)
{
/*重载输出运算符*/
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
/*重载加法，1*/
bigint lIntTmp = lInt;
bigint rIntTmp = rInt;
unsigned int lLen = lInt.len_;
unsigned int rLen = rInt.len_;
unsigned int count = 0;/*计算次数*/
int carry = 0;/*进位保存*/

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
/*重载加法，2*/
bigint tmp(str);
return (lInt + tmp);
}

bigint operator +(const string& str, const bigint& rInt)
{
/*重载加法，3*/
bigint tmp(str);
return (tmp + rInt);
}

bigint operator -(const bigint& lInt, const bigint& rInt)
{
/*重载减法，1*/
if (lInt < rInt)
{
   cout << "减法错误！";
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
/*重载减法，2*/
bigint tmp(str);
return (lInt - tmp);
}

bigint operator -(const string& str, const bigint& rInt)
{
/*重载减法，3*/
bigint tmp(str);
return (tmp - rInt);
}

bigint operator *(const bigint& lInt, const bigint& rInt)
{
/*重载乘法，1*/
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
/*重载乘法，2*/
bigint tmp(str);
return (lInt * tmp);
}

bigint operator *(const string& str, const bigint& rInt)
{
/*重载乘法，3*/
bigint tmp(str);
return (tmp * rInt);
}

bigint operator /(const bigint& lInt, const bigint& rInt)
{
/*重载除法，1*/
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
/*重载除法，2*/
bigint tmp(str);
return (lInt / tmp);
}

bigint operator /(const string& str, const bigint& rInt)
{
/*重载除法，3*/
bigint tmp(str);
return (tmp / rInt);
}

bigint operator %(const bigint& lInt, const bigint& rInt)
{
/*重载余法，1*/
return (lInt - rInt * (lInt / rInt));
}

bigint operator %(const bigint& lInt, const string& str)
{
/*重载余法，2*/
bigint tmp(str);
return (lInt - tmp * (lInt / tmp));
}

bigint operator %(const string& str, const bigint& rInt)
{
/*重载余法，3*/
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
/*去掉大数处理后前面多出的零，如果全为零，就留一个零*/
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
/*大数前面补零，方便计算*/
while (len--)
{
   cache_.push_back(0);
   len_++;
}
}

void bigint::addZeroTail_(unsigned int len)
{
/*大数后面补零，相当于乘10*/
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
