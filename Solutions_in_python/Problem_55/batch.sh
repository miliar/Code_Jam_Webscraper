python splitter.py $1

for i in $1.*; do
	python park.py $i > out.$i &
done

wait

cat out.$1.* | tee out.$1
