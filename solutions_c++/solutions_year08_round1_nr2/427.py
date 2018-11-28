#define Max(x, y) (x > y ? x : y)

template <class T>
class Queue;

template <class T>
class QList
{
private:
	T *object_;
	QList< T >* prev_;
	QList< T >* next_;

	QList()
	{
		object_ = NULL;
		prev_ = NULL;
		next_ = NULL;
	}

	~QList()
	{
		if(object_)
			delete object_;
	}

	friend class Queue< T >;
};

template <class T>
class Queue
{
private:
	QList<T> *head_;
	QList<T> *tail_;

	int count_;

	int indexmove_;
	QList<T> *listmove_;

public:
	Queue()
	{
		Init();
	}

	Queue(Queue< T >& queue)
	{
		Init();
		CopyBody(queue);
	}

	~Queue()
	{
		ClearUp();
	}

	Queue< T >& operator = (Queue< T >& queue)
	{
		ClearUp();
		Init();
		CopyBody(queue);

		return *this;
	}

	int IsEmpty()
	{
		if (count_ == 0)
			return 1;
		return 0;
	}

	void EnQueue(T* object)
	{
		EnQueueTail(object);
	}

	T* DeQueue()
	{
		return DeQueueHead();
	}

	T* Pop()
	{
		return DeQueueTail();
	}

	void EnQueueTail(T* object)
	{
		QList< T > *p = tail_->prev_, *list = new QList< T >;

		list->object_ = object;
			
		list->prev_ = p;
		list->next_ = tail_;
		p->next_ = list;
		tail_->prev_ = list;
		
		count_ ++;
	}

	void EnQueueHead(T* object)
	{
		QList< T > *p = head_->next_, *list = new QList< T >;
		
		list->object_ = object;
			
		list->prev_ = head_;
		list->next_ = p;
		head_->next_ = list;
		p->prev_ = list;

		if(indexmove_ > -1)
			indexmove_ ++;

		count_ ++;
	}

	T* DeQueueTail()
	{
		T* object;
		QList< T >* p;

		p = tail_->prev_;
		p->prev_->next_ = tail_;
		tail_->prev_ = p->prev_;

		if(indexmove_ == count_ - 1)
		{
			indexmove_ = -1;
			listmove_ = head_;
		}
	
		count_ --;

		object = p->object_;
		p->object_ = NULL;
		delete p;

		return object;
	}

	T* DeQueueHead()
	{
		T* object;
		QList< T >* p;

		p = head_->next_;
		p->next_->prev_ = head_;
		head_->next_ = p->next_;

		count_ --;

		if(indexmove_ > 0)
			indexmove_ --;
		else if(indexmove_ == 0)
		{
			indexmove_ = -1;
			listmove_ = head_;
		}

		object = p->object_;
		p->object_ = NULL;
		delete p;

		return object;
	}

	
	void Delete(int index)
	{
		QList< T > *p, *q, *list;

		MoveTo(index - 1);

		list = listmove_->next_;
		p = list->prev_;
		q = list->next_;
		p->next_ = q;
		q->prev_ = p;
		delete list;

		count_--;
	}

	T* DeQueueFrom(int index)
	{
		QList< T > *p, *q, *list;
		T* object;

		MoveTo(index - 1);

		list = listmove_->next_;
		p = list->prev_;
		q = list->next_;
		p->next_ = q;
		q->prev_ = p;

		count_--;
		
		object = list->object_;
		list->object_ = NULL;
		delete list;

		return object;
	}

	void InsertAs(T* object, int index)		//Insert as index
	{
		QList< T > *list, *p, *q;

		MoveTo(index - 1);

		list = new QList<T>;
		list->object_ = object;
		
		p = listmove_;
		q = p->next_;
		
		list->prev_ = p;
		list->next_ = q;
		p->next_ = list;
		q->prev_ = list;

		count_++;
	}

	T& operator [] (int index)
	{
		MoveTo(index);

		return *listmove_->object_;
	}
	
	void MoveTo(int index)
	{
		while(index > indexmove_)
		{
			listmove_ = listmove_->next_;
			indexmove_ ++;
		}

		while(index < indexmove_)
		{
			listmove_ = listmove_->prev_;
			indexmove_ --;
		}
	}

	int GetSize()
	{
		return count_;
	}

	T** GetObjectAddrs()
	{
		T** addr = new T* [count_];

		for(int i = 0; i < count_; i++)
			addr[i] = &(*this)[i];

		return addr;
	}

	void Merge(Queue< T >& queue)
	{
		while(! queue.IsEmpty())
			EnQueue(queue.DeQueue());
	}

private:
	void Init()
	{
		head_ = new QList< T >;
		tail_ = new QList< T >;
		head_->next_ = tail_;
		tail_->prev_ = head_;

		count_ = 0;
		indexmove_ = -1;
		listmove_ = head_;
	}

	void ClearUp()
	{
		QList< T > *p = head_;
		QList< T > *q;
		while(p)
		{
			q = p->next_;
			delete p;
			p = q;
		}
	}

	void CopyBody(Queue< T >& queue)
	{
		T* object;

		for(int i = 0; i < queue.count_; i++)
		{
			object = new T(queue[i]);
			EnQueueTail(object);
		}
	}
};


