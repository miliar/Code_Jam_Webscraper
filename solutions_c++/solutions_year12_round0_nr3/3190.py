 #include<iostream>
  #include<cmath>
 
 using namespace std;
 
 int main()
 {	unsigned int TestCases,A,B,Solution,NumberOfDigits,LSD,MSD,Recycled;
	cin>>TestCases;
	for(unsigned int TestCase = 0; TestCase < TestCases; ++TestCase)
	{	cin>>A>>B;
		Solution = 0;
		for(unsigned int Number = A; Number <= B; ++Number)
		{	NumberOfDigits = 0;
			MSD = Number;
			while(MSD)
			{	NumberOfDigits++;
				MSD /= 10;
			}
			MSD = 1;
			for(unsigned int Power = 1; Power < NumberOfDigits; ++Power)
				MSD *= 10;
			Recycled = Number;
			for(unsigned int Digit = 0; Digit < NumberOfDigits-1; ++Digit)
			{	LSD = Recycled%10;
				Recycled = Recycled/10 + LSD*MSD; 
				if(LSD && Recycled >= A && Recycled <= B && Recycled < Number)
					Solution++;
					
				
			}
			
		}
		cout<<"Case #"<<TestCase+1<<": "<<Solution<<"\n";
	}
	return 0;
}