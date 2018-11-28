#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
  ofstream f_output("output");
  ifstream f_input("input");

  int N;
  string wzor = "welcome to code jam";
  string s;
  f_input >> N;
  getline(f_input, s);

  for (int p=1; p<=N; p++)
    {
      getline(f_input, s);
      //cout << s << endl;
      int ilosc=0;
      //cout << s.size() << endl;
      for (int i1=0; i1 <= s.size(); i1++)
	{
	  if (s[i1]==wzor[0])
	    {
	      for (int i2=i1; i2 <= s.size(); i2++)
		{
		  if (s[i2]==wzor[1])
		    {
		      for (int i3=i2; i3 <= s.size(); i3++)
			{
			  if (s[i3]==wzor[2])
			    {
			      for (int i4=i3; i4 <= s.size(); i4++)
				{
				  if (s[i4]==wzor[3])
				    {
				      for (int i5=i4; i5 <= s.size(); i5++)
					{
					  if (s[i5]==wzor[4])
					    {
					      for (int i6=i5; i6 <= s.size(); i6++)
						{
						  if (s[i6]==wzor[5])
						    {
						      for (int i7=i6; i7 <= s.size(); i7++)
							{
							  if (s[i7]==wzor[6])
							    {
				 			      for (int i8=i7; i8 <= s.size(); i8++)
								{
								  if (s[i8]==wzor[7])
								    {
								      for (int i9=i8; i9 <= s.size(); i9++)
									{
									  if (s[i9]==wzor[8])
									    {
									      for (int i10=i9; i10 <= s.size(); i10++)
										{
										  if (s[i10]==wzor[9])
										    {
										      for (int i11=i10; i11 <= s.size(); i11++)
											{
											  if (s[i11]==wzor[10])
											    { 	
											      for (int i12=i11; i12 <= s.size(); i12++)
												{
												  if (s[i12]==wzor[11])
												    {
												      for (int i13=i12; i13 <= s.size(); i13++)
													{
													  if (s[i13]==wzor[12])
													    {
													      for (int i14=i13; i14 <= s.size(); i14++)
														{
														  if (s[i14]==wzor[13])
														    {
														      for (int i15=i14; i15 <= s.size(); i15++)
															{
															  if (s[i15]==wzor[14])
															    {
															      for (int i16=i15; i16 <= s.size(); i16++)
																{
																  if (s[i16]==wzor[15])
																    {
																      for (int i17=i16; i17 <= s.size(); i17++)
																	{
																	  if (s[i17]==wzor[16])
																	    {
																	      for (int i18=i17; i18 <= s.size(); i18++)
																		{
																		  if (s[i18]==wzor[17])
																		    {
																		      for (int i19=i18; i19 <= s.size(); i19++)
																			{
																			  if (s[i19]==wzor[18])
																			    {
																			      ilosc++;	      																			    }
																			}
																		    }
																		}
																	    }
																	}
																    }
																}
															    }
															}
														    }
														}
													    }
													}
												    }
												}     
											    }
											}     
										    }
										}     
									    }
									}     
								    }
								}     
							    }
							}     
						    }
						}     
					    }
					}
				    }
				}
			    }
			} 
		    }
		}
	    }
	}


      /*ostringstream ss;
 ss << ilosc;
 if ( ilosc > 999 )
 ss << ilosc;*/
 /* else
     if (ilosc > 99 )
       ss << ilosc << "0";
     else
       if (ilosc > 9 )
	 ss << ilosc << "00";
       else 
       ss << ilosc << "000";*/


      //string wyn = ss.str();

 f_output << "Case #" << p << ": ";
 /* for (int ii=0; ii<=3; ii++)
   {
     f_output << wyn[ii];
     }*/
 if ( ilosc >= 10000 )
   {
     f_output << ilosc%10000;
   }
 else
   if ( ilosc >= 1000 )
     f_output << ilosc;
   else
     if ( ilosc >= 100 )
       f_output << "0" << ilosc;
     else
       if ( ilosc >= 10 )
	 f_output << "00" << ilosc;
       else
	 f_output << "000" << ilosc;


 f_output << endl;
    }
  return 0;
}
