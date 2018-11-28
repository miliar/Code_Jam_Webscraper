#include"iostream.h"
#include"stdio.h"
int main()
{
	long int N,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,i,t,n;
	char c[500];
	FILE *fp;
	fp=fopen("D:\\SM\\Small.txt","w");
	cin>>N;
	for(i=0;i<N+1;i++)
	{
		cin.getline(c,500);
		n=strlen(c);
		t=0;
		for(a1=0;a1<n;a1++)
		{
			if(c[a1]=='w')
			{
				for(a2=a1+1;a2<n;a2++)
				{
					if(c[a2]=='e')
					{
						for(a3=a2+1;a3<n;a3++)
						{
							if(c[a3]=='l')
							{
								for(a4=a3+1;a4<n;a4++)
								{
									if(c[a4]=='c')
									{
										for(a5=a4+1;a5<n;a5++)
										{
											if(c[a5]=='o')
											{
												for(a6=a5+1;a6<n;a6++)
												{
													if(c[a6]=='m')
													{
														for(a7=a6+1;a7<n;a7++)
														{
															if(c[a7]=='e')
															{
																for(a8=a7+1;a8<n;a8++)
																{
																	if(c[a8]==' ')
																	{
																		for(a9=a8+1;a9<n;a9++)
																		{
																			if(c[a9]=='t')
																			{
																				for(a10=a9+1;a10<n;a10++)
																				{
																					if(c[a10]=='o')
																					{
																						for(a11=a10+1;a11<n;a11++)
																						{
																							if(c[a11]==' ')
																							{
																								for(a12=a11+1;a12<n;a12++)
																								{
																									if(c[a12]=='c')
																									{
																										for(a13=a12+1;a13<n;a13++)
																										{
																											if(c[a13]=='o')
																											{
																												for(a14=a13+1;a14<n;a14++)
																												{
																													if(c[a14]=='d')
																													{
																														for(a15=a14+1;a15<n;a15++)
																														{
																															if(c[a15]=='e')
																															{
																																for(a16=a15+1;a16<n;a16++)
																																{
																																	if(c[a16]==' ')
																																	{
																																		for(a17=a16+1;a17<n;a17++)
																																		{
																																			if(c[a17]=='j')
																																			{
																																				for(a18=a17+1;a18<n;a18++)
																																				{
																																					if(c[a18]=='a')
																																					{
																																						for(a19=a18+1;a19<n;a19++)
																																						{
																																							if(c[a19]=='m')
																																							t++;
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
		if(!i) ;
		else
		{
			t=t%10000;
			if(t>=0&&t<10)
			{
				cout<<"Case #"<<i<<": 000"<<t<<endl;
				fprintf(fp,"Case #%d: 000%d\n",i,t);
			}
			else if(t>=10&&t<100)
			{
			   cout<<"Case #"<<i<<": 00"<<t<<endl;
			   fprintf(fp,"Case #%d: 00%d\n",i,t);
			}
			else if(t>=100&&t<1000)
			{
			   cout<<"Case #"<<i<<": 0"<<t<<endl;
			   fprintf(fp,"Case #%d: 0%d\n",i,t);
			}
			else if(t>=1000&&t<10000)
			{
			   cout<<"Case #"<<i<<": "<<t<<endl;
			   fprintf(fp,"Case #%d: %d\n",i,t);
			}
        }
	}
	 system("pause");
	 fclose(fp);
}
