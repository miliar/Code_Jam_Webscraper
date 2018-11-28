    #include<fstream.h>
    #include<iostream.h>
    #include<conio.h>
    #include<string.h>
    #include<math.h>

    int count;
    int level;
    int n,l,d;
    char dict[16];
    char pattern[16][100];


    int search(char a[],char b)
    {
	int i,f=0;
	for(i=0;a[i]!='\0';i++)
	{
	    if(a[i]==b)
	    {
		f=1;
		break;
	    }
	}
	return f;
    }




    void main()
    {
    clrscr();

	int i,j,k,m;
	char data[2000];
	fstream fin,fout,fout1,fin1;
	fin.open("input.txt",ios::in);
	fout.open("output.txt",ios::out);
	fout1.open("temp.txt",ios::out);
	fin>>l;
	fin>>d;
	fin>>n;

	fin.getline(dict,100);

	for(i=0;i<d;i++)
	{
	fin.getline(dict,18);
	fout1<<dict<<endl;
	}
	fout1.close();

    for(m=1;m<=n;m++)
    {
	fin.getline(data,2000);
	//cout<<data<<endl;
	k=0;
	for(i=0;data[i]!='\0';i++)
	{
	    if(data[i]=='(')
	    {

		i++;
		for(j=0;data[i]!=')';j++,i++)
		pattern[k][j]=data[i];
		pattern[k][j]='\0';
		k++;

	     }
	    else
	    {
		pattern[k][0]=data[i];
		pattern[k][1]='\0';
		k++;
	    }
	}

    int length,flag1=1,count=0;
    fin1.open("temp.txt",ios::in);

    for(i=0;i<d;i++)
    {
	fin1.getline(dict,18);

	flag1=1;
	for(j=0;j<l;j++)
	{

	    if(search(pattern[j],dict[j])==0)
	    {
		flag1=0;
		break;
	    }
	}
	if(flag1==1)
	    count++;
    }



	fout<<"Case #"<<m<<": "<<count<<endl;

    fin1.close();
    }

    fin.close();
    fout.close();

	getch();

    }
