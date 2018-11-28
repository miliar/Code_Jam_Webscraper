class FLarge
{
private:
	int *data;
	int length;
	static FLarge Multiply(FLarge &lNumber, int rNumber);
public:
	FLarge();
	~FLarge();
	FLarge(FLarge &large);
	bool read(void);
	bool print(void);
	bool UpdateLength(void);
	int GetLength(void);
	FLarge &operator =(FLarge &other);
	FLarge operator +(FLarge &other);
	FLarge operator -(FLarge &other);
	FLarge operator *(FLarge &other);
	FLarge operator %(FLarge &other);
	FLarge operator <<(int n);
	bool operator < (FLarge &other);
	bool iszero();
};

FLarge::FLarge(void)
{
	data = new int [N];
	length = 0;
	int n = N;
	while (--n>=0)
	{
		data[n] = 0;
	}
}

FLarge::~FLarge(void)
{
	delete [] data;
}

FLarge::FLarge(FLarge &large)
{
	data = new int [N];
	for (int i = 0; i<N; i++)
	{	
		data[i] = large.data[i];
		length = large.GetLength();
	}
}

bool FLarge::read(void)
{
	int n = N;
	char tmp = '0';
	tmp = datain.get();
	while (--n>=0 && tmp>='0' && tmp<='9')
	{
		data[n] = tmp - '0';
		tmp = datain.get();
	}
	n++;
	length = N - n;
	for (int k = 0; k < length ;k++)
		data[k] = data[k + n];
	for (int k = length; k < N ;k++)
		data[k] = 0;
	return true;
}

bool FLarge::print(void)
{
	int n = N+1;
	while (data[--n-1]==0);
	if (n==0)
	{
		dataout<<'0';
	}
	else
	{
		while (--n>=0)
		{
			dataout<<data[n];
		}
	}
	return true;
}

int FLarge::GetLength()
{
	return length;
}

bool FLarge::UpdateLength()
{
	int n = N+1;
	while (data[--n-1]==0);
	length = n;
	return true;
}

FLarge FLarge::Multiply(FLarge &lNumber, int rNumber)
{
	FLarge result;
	for (int i = 0; i<lNumber.GetLength(); i++)
	{
		result.data[i] += lNumber.data[i] * rNumber;
		int j = i;
		while (result.data[j]>=10)
		{
			result.data[j+1]++;
			result.data[j] %= 10;
			j++;
		}
	}
	result.UpdateLength();
	return result;
}

FLarge &FLarge::operator =(FLarge &other)
{
	for (int i = 0; i<N; i++)
	{	
		data[i] = other.data[i];
	}
	UpdateLength();
	return *this;
}

FLarge FLarge::operator +(FLarge &other)
{
    FLarge result = *this;
    FLarge rNumber=other;
	for (int i = 0; i<N-1; i++)
	{	
		result.data[i] += rNumber.data[i];
		int j = i;
		while (result.data[j]>=10)
		{
			result.data[j+1]++;
			result.data[j] %= 10;
			j++;
		}
	}
	result.UpdateLength();
	return result;
}

FLarge FLarge::operator -(FLarge &other)
{
    FLarge result = *this;
    FLarge rNumber=other;
	for (int i = 0; i<N-1; i++)
	{	
		result.data[i] -= rNumber.data[i];
		int j = i;
		while (result.data[j]<0 && j<N)
		{
			result.data[j+1]--;
			result.data[j] += 10;
			j++;
		}
		if (j == N)
		{
			cout<<"minus overflow!"<<endl;
			return result;
		}
	}
	result.UpdateLength();
	return result;
}

FLarge FLarge::operator *(FLarge &other)
{
    FLarge result;
    FLarge lNumber=*this;
    FLarge rNumber=other;
	if (lNumber.GetLength() + rNumber.GetLength()> N)
	{	
		cout<<"multiply overflow!"<<endl;
		return result;
	}
	for (int i = 0; i<rNumber.GetLength(); i++)
	{	
		result = result + (Multiply(lNumber,rNumber.data[i]) << i);
	}
	result.UpdateLength();
	return result;
}

FLarge FLarge::operator %(FLarge &other)
{
    FLarge result = *this;
    FLarge rNumber = other;
	for (int shift = result.GetLength() - rNumber.GetLength(); shift>=0; shift--)
	{
		FLarge temp = rNumber << shift;
		while (! (result < temp))
		{
			result = result - temp;
		}
	}
	result.UpdateLength();
	return result;
}

FLarge FLarge::operator <<(int n)
{
    FLarge result;
	if (this->GetLength() + n > N)
	{
		cout<<"move overflow!"<<endl;
		return result;
	}
	for (int i = this->GetLength()-1; i>=0; i--)
	{
		result.data[i+n] = this->data[i];
	}
	result.UpdateLength();
	return result;
}

bool  FLarge::operator < (FLarge &other)
{
	if (this->length < other.GetLength())
		return true;
	else if (length > other.GetLength())
		return false;
	else
	{
		int l = length;
		while (data[l] == other.data[l] && l>=0)
		{
			l--;
		}
		if (l>=0 && data[l] < other.data[l] )
			return true;
		else
			return false;
	}
}

bool FLarge::iszero()
{
	return (length == 0);
}