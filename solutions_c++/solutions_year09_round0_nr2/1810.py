    #include<fstream.h>
    #include<iostream.h>
    #include<conio.h>
    #include<string.h>
    #include<math.h>

   char label[100][100];
   int a[100][100],l,b;
   char count='a';

    char recurse(int i,int j)
    {
	int lowest=0,mark=0;
	if(label[i][j]!=0)
	{
	    return label[i][j];
	}

		mark=0;
		lowest=a[i][j];
		if(i!=0)
		{
		    if(a[i-1][j]<lowest)
		    {
			mark=1;//north
			lowest=a[i-1][j];
		    }
		}
		if(j!=0)
		{
		    if(a[i][j-1]<lowest)
		    {
			mark=2;//west
			lowest=a[i][j-1];
		    }
		}
		if(j!=b-1)
		{
		    if(a[i][j+1]<lowest)
		    {
			mark=3;//east
			lowest=a[i][j+1];
		    }
		}
		if(i!=l-1)
		{
		    if(a[i+1][j]<lowest)
		    {
			mark=4;//south
			lowest=a[i+1][j];
		    }
		}
		switch(mark)
		{
		    case 0:label[i][j]=count;
			    count++;
			    return label[i][j];

		    case 1:label[i][j]=recurse(i-1,j);//north
		    break;
		    case 2:label[i][j]=recurse(i,j-1);//west
		    break;
		    case 3:label[i][j]=recurse(i,j+1);//east
		    break;
		    case 4:label[i][j]=recurse(i+1,j);//south
		    break;
		}
     return label[i][j];
    }

    void main()
    {
	clrscr();

	int i,j,m,n,x,y;


	fstream fin,fout;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);

    fin>>n;


    for(m=1;m<=n;m++)
    {
    fin>>l>>b;
    for(i=0;i<l;i++)
	{
	    for(j=0;j<b;j++)
	    fin>>a[i][j];
	}
	//fin.getline(data,32);
	for(i=0;i<l;i++)
	{
	    for(j=0;j<b;j++)
	    label[i][j]=0;
	}

    //int lowest=0,mark=0;
    for(x=0;x<l;x++)
	{
	    for(y=0;y<b;y++)
	    {
		recurse(x,y);
	    }
	}

    fout<<"Case #"<<m<<":\n";
    for(i=0;i<l;i++)
    {
    for(j=0;j<b;j++)
    {
	fout<<label[i][j];
	if(j!=b-1)
	{
	    fout<<" ";
	}
    }
    fout<<endl;
    }
    count='a';
    }
     fin.close();
     fout.close();

	cout<<"SUCESS"<<endl;
	getch();

    }
