class twoWords
{
private:
	unsigned int long long first;
	unsigned int long long second;
	unsigned int long long n1;
	unsigned int long long n2;
public:
        twoWords();
        void resetWords(int n);
	void resetWords();
	bool checkPos(int pos);
	bool updatePos(int pos); 
	bool areAllEnginesExhausted(int number);
};
