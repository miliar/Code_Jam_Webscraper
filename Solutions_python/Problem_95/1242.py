#/usr/bin/python
import io
convTable = "".maketrans("abcdefghijklmnopqrstuvwxyz", "yhesocvxduiglbkrztnwjpfmaq")
n = int(input())
for i in range(1,n+1):
	print("Case #{0}: {1}".format(i, input().translate(convTable)))
