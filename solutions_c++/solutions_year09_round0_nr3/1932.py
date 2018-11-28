#include<iostream.h>
#include<conio.h>
#include<string.h>
struct ch{
	    char c;
	    int num;
	    int pos[500];
	 };
void main()
{
	int N,p,count,w_in,e_in,l_in,c_in,o_in,m_in,e2_in,sp_in,t_in,o2_in,sp2_in,c2_in,o3_in,d_in,e3_in,sp3_in,j_in,a_in,m2_in,flag;
	char string[505],q,flush,output[100][5];
	ch w = {'w',0,};
	ch e = {'e',0,};
	ch l = {'l',0,};
	ch c = {'c',0,};
	ch o = {'o',0,};
	ch m = {'m',0,};
	ch sp = {' ',0,};
	ch t = {'t',0,};
	ch d = {'d',0,};
	ch j = {'j',0,};
	ch a = {'a',0,};
	cin>>N;
	cin.get(flush);
	for(int i=0;i<N;i++)
	{
		w.num=e.num=l.num=c.num=o.num=m.num=sp.num=t.num=d.num=j.num=a.num=0;
		count=0;
		cin.getline(string,505);
		p=0;q='a';
		while(q!='\0')
		{
			q=string[p];
			switch(q)
			{
				case 'w':w.pos[w.num]=p;
					 w.num++;break;
				case 'e':if(w.num)
							{
									e.pos[e.num]=p;
									e.num++;
							}break;
				case 'l':if(e.num)
							{
								l.pos[l.num]=p;
								l.num++;
							}break;
				case 'c':if(l.num)
							{
							c.pos[c.num]=p;
								c.num++;
							}break;
				case 'o':if(c.num)
							{
								o.pos[o.num]=p;
								o.num++;
							}break;
				case 'm':if(o.num)
							{
								m.pos[m.num]=p;
								m.num++;
							}break;
				case ' ':if(m.num)
							 {
								sp.pos[sp.num]=p;
								sp.num++;
							 }break;
				case 't':if(sp.num)
							{
								t.pos[t.num]=p;
								t.num++;
							}break;
				case 'd':if(t.num)
							{
								d.pos[d.num]=p;
								d.num++;
							}break;
				case 'j':if(d.num)
							{
								j.pos[j.num]=p;
								j.num++;
							}break;
				case 'a':if(j.num)
							{
								a.pos[a.num]=p;
								a.num++;
							}break;
			}
			p++;
		}
		flag=1;
		for(w_in=0;w_in<w.num;)
		{
			for(e_in=0;e_in<e.num;)
			{
				while(e.pos[e_in]<w.pos[w_in])
					{e_in++;if(e_in==e.num)flag=0;}
				if(!flag){flag=1;break;}
				for(l_in=0;l_in<l.num;)
				{
					while(l.pos[l_in]<e.pos[e_in])
						{l_in++;if(l_in==l.num)flag=0;}
					if(!flag){flag=1;break;}
					for(c_in=0;c_in<c.num;)
					{
						while(c.pos[c_in]<l.pos[l_in])
							{c_in++;if(c_in==c.num)flag=0;}
						if(!flag){flag=1;break;}
						for(o_in=0;o_in<o.num;)
						{
							while(o.pos[o_in]<c.pos[c_in])
								{o_in++;if(o_in==o.num)flag=0;}
							if(!flag){flag=1;break;}
							for(m_in=0;m_in<m.num;)
							{
								while(m.pos[m_in]<o.pos[o_in])
									{m_in++;if(m_in==m.num)flag=0;}
								if(!flag){flag=1;break;}
								for(e2_in=0;e2_in<e.num;)
								{
									while(e.pos[e2_in]<m.pos[m_in])
										{e2_in++;if(e2_in==e.num)flag=0;}
									if(!flag){flag=1;break;}
									for(sp_in=0;sp_in<sp.num;)
									{
										while(sp.pos[sp_in]<e.pos[e2_in])
											{sp_in++;if(sp_in==sp.num)flag=0;}
										if(!flag){flag=1;break;}
										for(t_in=0;t_in<t.num;)
										{
											while(t.pos[t_in]<sp.pos[sp_in])
												{t_in++;if(t_in==t.num)flag=0;}
											if(!flag){flag=1;break;}
											for(o2_in=0;o2_in<o.num;)
											{
												while(o.pos[o2_in]<t.pos[t_in])
													{o2_in++;if(o2_in==o.num)flag=0;}
												if(!flag){flag=1;break;}
												for(sp2_in=0;sp2_in<sp.num;)
												{
													while(sp.pos[sp2_in]<o.pos[o2_in])
														{sp2_in++;if(sp2_in==sp.num)flag=0;}
													if(!flag){flag=1;break;}
													for(c2_in=0;c2_in<c.num;)
													{
														while(c.pos[c2_in]<sp.pos[sp2_in])
															{c2_in++;if(c2_in==c.num)flag=0;}
														if(!flag){flag=1;break;}
														for(o3_in=0;o3_in<o.num;)
														{
															while(o.pos[o3_in]<c.pos[c2_in])
																{o3_in++;if(o3_in==o.num)flag=0;}
															if(!flag){flag=1;break;}
															for(d_in=0;d_in<d.num;)
															{
																while(d.pos[d_in]<o.pos[o3_in])
																	{d_in++;if(d_in==d.num)flag=0;}
																if(!flag){flag=1;break;}
																for(e3_in=0;e3_in<e.num;)
																{
																	while(e.pos[e3_in]<d.pos[d_in])
																		{e3_in++;if(e3_in==e.num)flag=0;}
																	if(!flag){flag=1;break;}
																	for(sp3_in=0;sp3_in<sp.num;)
																	{
																		while(sp.pos[sp3_in]<e.pos[e3_in])
																			{sp3_in++;if(sp3_in==sp.num)flag=0;}
																		if(!flag){flag=1;break;}
																		for(j_in=0;j_in<j.num;)
																		{
																			while(j.pos[j_in]<sp.pos[sp3_in])
																				{j_in++;if(j_in==j.num)flag=0;}
																			if(!flag){flag=1;break;}
																			for(a_in=0;a_in<a.num;)
																			{
																				while(a.pos[a_in]<j.pos[j_in])
																					{a_in++;if(a_in==a.num)flag=0;}
																				if(!flag){flag=1;break;}
																				for(m2_in=0;m2_in<m.num;)
																				{
																					while(m.pos[m2_in]<a.pos[a_in])
																						{m2_in++;if(m2_in==m.num)flag=0;}
																					if(!flag){flag=1;break;}
																					count++;
																					m2_in++;
																					count=count%10000;
																				}
																				a_in++;
																			}
																			j_in++;
																		}
																		sp3_in++;
																	}
																	e3_in++;
																}
																d_in++;
															}
															o3_in++;
														}
														c2_in++;
													}
													sp2_in++;
												}
												o2_in++;
											}
											t_in++;
										}
										sp_in++;
									}
									e2_in++;
								}
								m_in++;
							}
							o_in++;
						}
						c_in++;
					}
					l_in++;
				}
				e_in++;
			}
			w_in++;
		}
		output[i][4]='\0';
		output[i][3]=(count%10)+'0';
		count=count/10;
		output[i][2]=(count%10)+'0';
		count=count/10;
		output[i][1]=(count%10)+'0';
		count=count/10;
		output[i][0]=(count%10)+'0';

	}
	for(i=0;i<N;i++)
	{
		cout<<"Case #"<<i+1<<": "<<output[i]<<"\n";
	}
}


